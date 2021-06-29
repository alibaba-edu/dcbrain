import pickle
from AIHS_Training import Mapper, Predictor, Controller
class AIHS_api():
    def __init__(self, mapper_file, predictor_file, controller_file):
        with open(mapper_file, 'rb') as f:
            self.mapper=pickle.load(f)
        with open(predictor_file, 'rb') as f:
            self.predictor=pickle.load(f)
        with open(controller_file, 'rb') as f:
            self.controller=pickle.load(f) 
    
    #msg_dict, contains the online information, include attributes, hostname, timestamp and so on.
    def healing_process(self, msg_dict):
        attribute=msg_dict['attribute_str']
        result_dict={}
        result_dict['hostname'] = msg_dict['hostname']
        result_dict['timestamp'] = msg_dict['timestamp']
        
        feature=self.mapper.Map([attribute])
        pre_action=self.predictor.predict(feature)
        final_action=self.controller.control(feature, pre_action)
        result_dict['action']=final_action
        
        return result_dict

    
if __name__=='__main__':
    service1=AIHS_api('./model/mapper.pkl','./model/predictor.pkl','./model/controller.pkl')
    
    #test sample
    msg={
        'hostname': '12x8dj02',
        'attribute_str':'attributes_0=good$attributes_1=good$attributes_2=warning$attributes_3=warning$attributes_4=critical$attributes_5=warning$attributes_6=info$attributes_7=good$attributes_8=fatal$attributes_9=critical$attributes_10=info$attributes_11=info$attributes_12=good$attributes_13=fatal$attributes_14=error$attributes_15=info$attributes_16=fatal$attributes_17=info$attributes_18=warning$attributes_19=fatal$attributes_20=warning$attributes_21=error$attributes_22=fatal$attributes_23=error$attributes_24=info$attributes_25=fatal$attributes_26=error$attributes_27=critical$attributes_28=good$attributes_29=critical$attributes_30=error$attributes_31=error$attributes_32=critical$attributes_33=error$attributes_34=info$attributes_35=good$attributes_36=critical$attributes_37=critical$attributes_38=info$attributes_39=critical$attributes_40=good$attributes_41=critical$attributes_42=error$attributes_43=good$attributes_44=info$attributes_45=fatal$attributes_46=good$attributes_47=good$attributes_48=error$attributes_49=fatal$attributes_50=error$attributes_51=good$attributes_52=fatal$attributes_53=info$attributes_54=warning$attributes_55=error$attributes_56=info$attributes_57=warning$attributes_58=good$attributes_59=good$attributes_60=fatal$attributes_61=critical$attributes_62=warning$attributes_63=warning$attributes_64=critical$attributes_65=critical$attributes_66=fatal$attributes_67=error$attributes_68=good$attributes_69=critical$attributes_70=warning$attributes_71=fatal$attributes_72=critical$attributes_73=critical$attributes_74=fatal$attributes_75=error$attributes_76=info$attributes_77=critical$attributes_78=good$attributes_79=error$attributes_80=error$attributes_81=info$attributes_82=info$attributes_83=fatal$attributes_84=warning$attributes_85=info$attributes_86=warning$attributes_87=warning$attributes_88=good$attributes_89=critical$attributes_90=error$attributes_91=critical$attributes_92=fatal$attributes_93=error$attributes_94=info$attributes_95=warning$attributes_96=error$attributes_97=info$attributes_98=info$attributes_99=info$attributes_100=warning$attributes_101=info$attributes_102=info$attributes_103=fatal$attributes_104=info$attributes_105=info$attributes_106=warning$attributes_107=fatal$attributes_108=critical$attributes_109=error$attributes_110=critical$attributes_111=critical$attributes_112=fatal$attributes_113=good$attributes_114=fatal$attributes_115=info$attributes_116=warning$attributes_117=error$attributes_118=warning$attributes_119=warning$attributes_120=fatal$attributes_121=error$attributes_122=fatal$attributes_123=fatal$attributes_124=good$attributes_125=critical$attributes_126=critical$attributes_127=fatal$attributes_128=critical$attributes_129=error$attributes_130=info$attributes_131=error$attributes_132=critical$attributes_133=info$attributes_134=good$attributes_135=info$attributes_136=critical$attributes_137=info$attributes_138=fatal$attributes_139=critical$attributes_140=critical$attributes_141=warning$attributes_142=good$attributes_143=fatal$attributes_144=critical$attributes_145=error$attributes_146=fatal$attributes_147=warning$attributes_148=error$attributes_149=info$attributes_150=error$attributes_151=error$attributes_152=error$attributes_153=critical$attributes_154=fatal$attributes_155=error$attributes_156=critical$attributes_157=info$attributes_158=fatal$attributes_159=critical$attributes_160=info$attributes_161=good$attributes_162=fatal$attributes_163=info$attributes_164=fatal',
        'timestamp':12345,
    }
    
    result=service1.healing_process(msg)
    print(result)
    
    
