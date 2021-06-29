import random
import numpy as np
import pandas as pd
random.seed(2020)
import pickle
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import lightgbm as lgb
import copy
pd.options.mode.chained_assignment = None

#In case of using Bert encoder, please reference the pretraining and extracting features processes of Bert (adds)
#Here we provide LDA and TF-IDF process
class Mapper():
    def __init__(self, mappper_type,df):
        #only used in LDA mapper.
        self.frequency_dict={'info':0,'good':1,'warning':2,'error':3,'critical':4,'fatal':5}
        
        self.type=mappper_type
        if self.type=='LDA':
            self.train_mapper_LDA(df)
        else:
            if self.type=='TFIDF':
                self.train_mapper_TFIDF(df)
            else:
                print("unsupport mapper type")
        self.mapper_function={
            'LDA': self._lda_mapper,
            'TFIDF': self._tfidf_mapper
        }
    
    def _lda_mapper(self, corpus):
        tf=self.vectorizer.transform(corpus)
        doc_topic_dist=self.lda.transform(tf)
        return doc_topic_dist
    
    def _tfidf_mapper(self, corpus):
        tfidf=self.vectorizer.transform(corpus)
        return tfidf.toarray()
    
    def _attributes_deal(self, attributes):
        document_str=""
        #    Transform attributes to documents where attribute name and its level combined as a word.
        if self.type=='LDA':
            dataarray=attributes.split('$')
            i=0
            for a in dataarray:
                m_str=a.split('=')[0]
                v_str=a.split('=')[1]
                document_str+=(m_str+" ")*self.frequency_dict[v_str]
        # Transform attributes to documents where attribute name as word and level as frequency
        else:
            dataarray=attributes.split('$')
            for a in dataarray:
                document_str+=(a+" ")
            
        return document_str
    
    def Mapdf(self, df):
        df=df.apply(self.AttributesTransform,axis=1)
       
        corpus=df.loc[:,['documents']].values.tolist()
        corpus=[y for x in corpus for y in x]
        features=self.mapper_function[self.type](corpus)
        return features   
    
    def Map(self, attributes):
        corpus=[self._attributes_deal(attribute) for attribute in attributes]
        features=self.mapper_function[self.type](corpus)
        return features
    
    def train_mapper_LDA(self, df):
        df=df.apply(self.AttributesTransform,axis=1)
        print("Transform completed")

        from sklearn.feature_extraction.text import CountVectorizer
        tf_vectorizer=CountVectorizer(min_df=1,max_df=1.0, lowercase=False, token_pattern='\\b\\w+\\b')

        corpus=df.loc[:,['documents']].values.tolist()
        corpus=[y for x in corpus for y in x]

        TF=tf_vectorizer.fit_transform(corpus)
        print('tf process completed')

        from sklearn.decomposition import LatentDirichletAllocation
        n_topics = 10
        lda= LatentDirichletAllocation(n_components=n_topics,
                                      doc_topic_prior=0.1,
                                      topic_word_prior=0.01,
                                      max_iter=100,
                                      evaluate_every=100,
                                      n_jobs=-1,
                                      learning_method='batch')
        lda.fit(TF)
        self.vectorizer=tf_vectorizer
        self.lda=lda

    def train_mapper_TFIDF(self, df):
        df=df.apply(self.AttributesTransform,axis=1)
        print("Transform completed")

        from sklearn.feature_extraction.text import TfidfVectorizer
        vectorizer=TfidfVectorizer()
        corpus=df.loc[:,['documents']].values.tolist()
        corpus=[y for x in corpus for y in x]

        vectorizer.fit(corpus)
        self.vectorizer=vectorizer
        
    def AttributesTransform(self, series):
        series['documents']=self._attributes_deal(series['attributes'])
        return series
    
    def savefiles(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
            
class Predictor():
    def __init__(self, df, mapper, predictor_type):
        self.mapper=mapper
        self.clf_obj_dict={
            'gbdt':lgb.LGBMClassifier(boosting_type='gbdt', num_leaves=1024, max_depth=-1,
                                     n_estimators=2000, objective='multiclass', subsample=0.8, learning_rate=0.2,
                                     random_state=2020, n_jobs=8, class_weight='balanced') ,
            'randomforest': RandomForestClassifier(n_estimators=1000, max_depth=10, class_weight='balanced', 
                                                   n_jobs=8, max_features='sqrt', random_state=2020),
            'naivebayes': GaussianNB(priors=None, var_smoothing=1e-09),
            'logisticregression':linear_model.LogisticRegression(solver='saga', max_iter=1024),
            'svm':SVC(decision_function_shape='ovo',gamma='auto')
        }
        if predictor_type in self.clf_obj_dict.keys():
            self.clf=self.clf_obj_dict[predictor_type]
        else:
            print('unsupport predictor type')
            return
        self.train_predictor(df)
    
    def predict(self,features):
        results=self.clf.predict(features)
        results=self.le.inverse_transform(results)
        return results
    
    def train_predictor(self,df):
        features=self.mapper.Mapdf(df)
        
        from sklearn import preprocessing
        self.le=preprocessing.LabelEncoder()
        self.le.fit(df.action.unique())
        labels=self.le.transform(df.action.values.tolist())
        self.clf.fit(features,labels)
    
    def savefiles(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

class Controller():
    def __init__(self, mapper, df, controller_type, actionlist=['NOP','MSR','ER','RB','RI','RMA']):
        self.actionlist=actionlist
        self.mapper=mapper
        self.type=controller_type
        
        self.clf_obj_dict={
            'gbdt':lgb.LGBMClassifier(boosting_type='gbdt', num_leaves=1024, max_depth=-1,
                                     n_estimators=2000, objective='binary', subsample=0.8, learning_rate=0.2,
                                     random_state=2020, n_jobs=8, class_weight='balanced') ,
            'randomforest': RandomForestClassifier(n_estimators=1000, max_depth=10, class_weight='balanced', 
                                                   n_jobs=8, max_features='sqrt', random_state=2020),
            'naivebayes': GaussianNB(priors=None, var_smoothing=1e-09),
            'logisticregression':linear_model.LogisticRegression(solver='saga', max_iter=1024),
            'svm':SVC(decision_function_shape='ovo',gamma='auto')
        }
        if self.type not in self.clf_obj_dict.keys():
            print('unsupport controller type')
            return None
        self.classifiers={}
        self.init_controller(df)
    
    def init_controller(self, df):
        for action in self.actionlist:
            df_current=df.loc[df.action==action]
            if df_current.shape[0]==0:
                print('No data of' + action)
                continue
            else:
                tmp_clf=self.train_binary_classifier(df_current)
                self.classifiers[action]=tmp_clf
    
    #process of a single instance
    def _control_process(self, feature, pre_action):
        pred=self.classifiers[pre_action].predict([feature])[0]
        if pred==1:
            return pre_action
        else:
            current_level=0
            current_action=self.actionlist[current_level]
            while current_level<len(self.actionlist):
                if self.classifiers[current_action]==1:
                    break
                else:
                    current_level+=1
                    if current_level>=len(self.actionlist):
                        current_action='call human'
                    else:
                        current_action=self.actionlist[current_level]
            return current_action
    
    #process instances
    def control(self, features, pre_actions):
        assert len(features)==len(pre_actions)
        final_actions=[]
        for index,pre_action in enumerate(pre_actions):
            final_action=self._control_process(features[index],pre_action)
            final_actions.append(final_action)
        return final_actions
    
    def train_binary_classifier(self, df):
        df_healthy = df.loc[df.final_state=='successful']
        df_failed = df.loc[df.final_state=='unsuccessful']
        
        if df_healthy.shape[0]==0 or df_failed.shape[0]==0:
            print('data absent')
            return None

        df_healthy.loc[:,'label']=1
        df_failed['label']=0

        df_training=pd.concat([df_healthy, df_failed],sort=False)

        features=self.mapper.Mapdf(df_training)
        labels=df_training.label.values.tolist()

        clf=copy.deepcopy(self.clf_obj_dict[self.type])
        
        clf.fit(features, labels)
        
        return clf
    
    def savefiles(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    
if __name__=='__main__':
    df=pd.read_csv('./dataset/train.csv')
    mapper=Mapper('LDA',df)
    mapper.savefiles('./model/mapper.pkl')
    predictor=Predictor(df,mapper,'gbdt')
    predictor.savefiles('./model/predictor.pkl')
    controller=Controller(mapper,df,'gbdt')
    controller.savefiles('./model/controller.pkl')
    print('training completed')
