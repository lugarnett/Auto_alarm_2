# -*- coding: gbk -*-
'''����acc���ݣ���ɿ��ٷ���'''
import gl
import time
from Afa_mainView import afa_mainview

from ruleLib.rule1 import rule_1
from ruleLib.rule2 import rule_2
from ruleLib.rule3 import rule_3
from ruleLib.rule4 import rule_4
from ruleLib.rule5 import rule_5
from ruleLib.rule6 import rule_6
from ruleLib.rule7 import rule_7
from ruleLib.rule8 import rule_8
from ruleLib.rule9 import rule_9
from ruleLib.rule10 import rule_10
from ruleLib.rule11 import rule_11
from ruleLib.rule12 import rule_12
from ruleLib.rule13 import rule_13
from ruleLib.rule14 import rule_14
from ruleLib.rule15 import rule_15
from ruleLib.rule16 import rule_16
from ruleLib.rule17 import rule_17
from ruleLib.rule18 import rule_18
from ruleLib.rule19 import rule_19

from ruleLib.rule50 import rule_50
from ruleLib.rule51 import rule_51
from ruleLib.rule52 import rule_52
from ruleLib.rule53 import rule_53
#from ruleLib.rule54 import rule_54

from ruleLib.rule80 import rule_80
from ruleLib.rule81 import rule_81
from ruleLib.rule82 import rule_82

#from findLib.find1 import find_1

from dbLib.accLib import Access_Model
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib as mpl
import collections
import os
import datetime

Anlyinmap = collections.OrderedDict()  
Drawinmap = collections.OrderedDict()  
rules = []

List_tbl = []
dataUrl = os.getcwd()+"\\dbLib\\data.mdb"
data = Access_Model(dataUrl)

def gettime():
    return time.strftime("%Y%m%d_%H:%M",time.localtime(time.time()))
def getdate(): 
    return time.strftime('%Y%m%d',time.localtime(time.time()))

'''1)��ȡList_tbl'''
def get_List_tbl():
    global List_tbl
    try:
        List_tbl.clear()

        sql = "SELECT Name FROM MSysObjects Where Type=1 ORDER BY Name"
        dataRecordSet = data.db_query(sql)
        #ȫ��������ȥ��ϵͳ����
        for item in dataRecordSet:
            a = eval("("+item+")")
            tblname = a['Name']
            if tblname.count('MSys') >= 1:
                continue
            elif tblname.count('0') >= 1 or tblname.count('6') >= 1:
                List_tbl.append(tblname)
        #end for
    except Exception as e:
        print(e)
    #print(List_tbl)
#endof 'mdl'
        
'''2.1)��ȡacc_tbl�Ľ�������'''
def acc_tbl_read(code):
    global Anlyinmap, Drawinmap
    
    #Outmap.clear()
    Anlyinmap.clear()
    Drawinmap.clear()

    ##�о���ĵ�����Ϊkey
    try:
        #��ȡrow_cnt
        sql = "SELECT COUNT(date) FROM %s"%code
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            row = int(a['Expr1000'])
        #end for
        
        '''���ݷ������������������ֹdate'''
        enddate = datetime.datetime.now()
        startdate = enddate + datetime.timedelta(days = - gl.Analyse_days)  #��n��
        startdate = startdate.strftime("%Y-%m-%d")
        enddate = enddate.strftime("%Y-%m-%d")
        #print(startdate)
        
        if row > 0:
            sql = "Select * FROM %s WHERE date BETWEEN #%s# and #%s# ORDER BY date"%(code,startdate,enddate) 
            dataRecordSet = data.db_query(sql)
            #Anlyinmap��keyΪi++���
            i = 1
            for item in dataRecordSet:
                a = eval("("+item+")")    #eval����JSON����
                '''
                ##############################################################
                #��ʱ�������ݸ�ʽ������Anlyinmap
                #�Ȱ���Ȩ���ݴ������账���޸�Ȩ���ݣ����ڴ��滻�����ٴε��ã�
                Anlyinmap[i] = {'date':a['date'][0:10], \
                '��K':[float(a['��1']), float(a['��1']), float(a['��1']), float(a['��1'])], \
                'V':[float(a['��']), float(a['���']), float(a['p_change'])], \
                'V_ma':[float(a['v_ma5']), float(a['v_ma10']), float(a['v_ma20'])], \
                '��':float(a['��']), \
                '��':[float(a['fma5']), float(a['fma10']), float(a['fma20']), float(a['fma30']), float(a['fma60'])], \
                
                '��K0':[float(a['��0']), float(a['��0']), float(a['��0']), float(a['��0'])], \
                '��0':[float(a['ma5']), float(a['ma10']), float(a['ma20']), float(a['ma30']), float(a['ma60'])]}
                ##############################################################
                '''
                ##############################################################
                #��ʱ�������ݸ�ʽ������Anlyinmap
                #�Ȱ���Ȩ���ݴ������账���޸�Ȩ���ݣ����ڴ��滻�����ٴε��ã�
                Anlyinmap[i] = {'date':a['date'][0:10], \
                '��K':[float(a['��0']), float(a['��0']), float(a['��0']), float(a['��0'])], \
                'V':[float(a['��']), float(a['���']), float(a['p_change'])], \
                'V_ma':[float(a['v_ma5']), float(a['v_ma10']), float(a['v_ma20'])], \
                '��':float(a['��']), \
                '��':[float(a['ma5']), float(a['ma10']), float(a['ma20']), float(a['ma30']), float(a['ma60'])]}
                ##############################################################
                
                #��ȡ���������������ݣ������K����Ϣ�棩��������key����outmap
                
                i = i + 1
                ##����������ʱ��ֹͣ��ȡ����
                if i >= gl.Analyse_days:
                    break
                #end if
            #end for
            print("%s���ȡ�ɹ���"%code)
            #print(Anlyinmap)
            
            #���ݴ���Drawinmap
            for (i,x) in Anlyinmap.items():
                Drawinmap[x['date']] = x
            #end for
            
            return 1
        else:
            print("%s������row=0����������"%code)
            return -1
        #end if
    except Exception as e:
        print(e)
        print("%s���ȡʧ�ܡ���������"%code)
        return -1

#end of "def"


'''2.2)��ȡrules'''
def afa_ruleget(code):
    global rules
    
    #������Ϊ���� �ַ��������Ӧ�ĺ���������
    
    if 1==1:
        rules.append({'һ��������', 'rule1'})
    if 1==2:
        rules.append({'�Ϳ�����', 'rule2'})
#end of "def"


'''2.3)�������ݷ���'''
def afa_ruleanlys(code):
    #��������
    if 1:
        '''rule_1(code, Anlyinmap)
        rule_2(code, Anlyinmap)
        rule_3(code, Anlyinmap)
        #rule_4(code, Anlyinmap)
        rule_5(code, Anlyinmap)
        #rule_6(code, Anlyinmap)
        rule_7(code, Anlyinmap)
        rule_8(code, Anlyinmap)
        rule_9(code, Anlyinmap)
        rule_10(code, Anlyinmap)
        #rule_11(code, Anlyinmap)
        rule_12(code, Anlyinmap)
        rule_13(code, Anlyinmap)
        rule_14(code, Anlyinmap)
        rule_15(code, Anlyinmap)
        rule_16(code, Anlyinmap)
        rule_17(code, Anlyinmap)
        rule_18(code, Anlyinmap)'''
        rule_19(code, Anlyinmap)
    #end if

    #ר�ò��ԣ����м���
    if 0:
        rule_50(code, Anlyinmap) #С���м��ͣ�5��3��
        rule_51(code, Anlyinmap) #С���м��ͣ�6��3��
        rule_52(code, Anlyinmap) #����м��ͣ���ͣ����Ӱ����ͣ��
        rule_53(code, Anlyinmap) #����м��ͣ�����˫��Ӱ��
        #rule_54(code, Anlyinmap) #
    #end if
        
    #��ϲ���
    if 0:
        rule_80(code, Anlyinmap) #10������ƽ����ͣƽ̨����(36��)
    #end if
        
    #�ɷ���Ѽͷ
    if 0:
        rule_81(code, Anlyinmap) #�ɷ���Ѽͷ(31��)
    #end if
    
    #ͨ��Ѽͷ(ʱ�䴰��>=6��)
    if 0:
        rule_82(code, Anlyinmap, 30)
        rule_82(code, Anlyinmap, 20)
        rule_82(code, Anlyinmap, 10)
        rule_82(code, Anlyinmap, 6)
    #end if
#end of "def"


#main����
def afa_proc_analyse():
    global List_tbl, Drawinmap

    if os.path.exists(gl.path_rule_rst) <= 0:    #�ж�Ŀ���Ƿ����
        os.mkdir(gl.path_rule_rst)
    if os.path.exists(gl.path_view_rst) <= 0:    #�ж�Ŀ���Ƿ����
        os.mkdir(gl.path_view_rst)
        
    head = '\x00\x00'  #512
    with open(gl.path_view_rst + '����code_' + getdate() + ".sel", 'a') as out:
        out.write(head)
          
        
    #1)��ȡ������list������codes�б��п������ݲ�ȫ��  
    get_List_tbl()
    
    
    ############    List_tbl = ['600068']################################
    #2����list����ȡÿ��tbl�����ݣ�������
    sumn = len(List_tbl)
    n = 0
    for code in List_tbl:
        n = n + 1
        print('\n��ʼ����%s (%d: %d) .............'%(code, sumn, n))
        gl.STCode = code
        #2.1)��ȡtbl���ݣ�����Anlyinmap      
        flag = acc_tbl_read(code)
        if flag == 1:
            afa_ruleget(code)
            afa_ruleanlys(code)
            afa_mainview(Drawinmap)
            print("3:rules������ϣ�")
        else:
            print("3:rules���������ݡ�����")    
    #end for
#endof 'mdl'

#main
afa_proc_analyse()
