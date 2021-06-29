import random
import numpy as np
import pandas as pd
random.seed(2020)

class DataGenerator():
    def __init__(self, actionlist=['NOP','MSR','ER','RB','RI','RMA'],
                 levels=['info','good','warning','error','critical','fatal']
                 , attributes_num=165):
        self.actionlist=actionlist
        self.attributes_num=attributes_num
        self.levels=levels
        self.states=['successful','unsuccessful']
    
    def gen_attributes(self):
        attribute_str=""
        for i in range(self.attributes_num):
            attribute_str+="attributes_"+str(i)+'='+self.levels[random.randint(0,5)]+'$'
        return attribute_str[:-1]
    
    def gen_data(self, data_num, file_name):
        action_list=[self.actionlist[random.randint(0,len(self.actionlist)-1)] for i in range(data_num)]
        attributes_list=[self.gen_attributes() for i in range(data_num)]
        final_states_list=[self.states[random.randint(0,1)] for i in range(data_num)]
        
        df=pd.DataFrame({'attributes':attributes_list,'action':action_list,'final_state':final_states_list})
        
        df.to_csv(file_name, encoding = 'utf8')
        return df

if __name__=='__main__':
    DG=DataGenerator()
    df=DG.gen_data(500,'./dataset/train.csv')
    #print(df.loc[(df.action=='NOP') & (df.final_state=='successful')])
    print("Synetic dataset generated finished!")
