# -*- coding: gbk -*-
'''����acc���ݣ���ɿ��ٷ���'''
import gl
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
from ruleLib.rule80 import rule_80
from ruleLib.rule81 import rule_81
from ruleLib.rule82 import rule_82

from findLib.find1 import find_1

from dbLib.accLib import Access_Model
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib as mpl
import collections
import os
import datetime

Outmap = collections.OrderedDict()  
Anlyinmap = collections.OrderedDict()  
rules = []

List_tbl = []
dataUrl = os.getcwd()+"\\dbLib\\data.mdb"
data = Access_Model(dataUrl)
##
Analyse_days = 20

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
    global Anlyinmap, Analyse_days
    
    #Outmap.clear()
    Anlyinmap.clear()

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
        startdate = datetime.datetime.now()
        #.strftime("%Y-%m-%d")  
        #print(startdate)
        #startdate = datetime.date(y, m, d)  #str -> datetime
        startdate = startdate + datetime.timedelta(days = -20)  #��n��
        startdate = (startdate.strftime("%Y-%m-%d"))
        #print(startdate)
        
        if row > 0:
            sql = "Select * FROM %s WHERE date>%s ORDER BY date"%(code, startdate) 
            dataRecordSet = data.db_query(sql)
            #Anlyinmap��keyΪi++���
            i = 0
            for item in dataRecordSet:
                a = eval("("+item+")")    #eval����JSON����
                
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

                #��ȡ���������������ݣ������K����Ϣ�棩��������key����outmap
                
                i = i + 1
                ##����������ʱ��ֹͣ��ȡ����
                if i >= Analyse_days:
                    break
                #end if
            #end for
            print("\n%s���ȡ�ɹ���"%code)
            #print(Anlyinmap)
            return 1
        else:
            print("\n%s������row=0����������"%code)
            return -1
        #end if
    except Exception as e:
        print(e)
        print("\n%s���ȡʧ�ܡ���������"%code)
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
    #print(Anlyinmap)
    rule_1(code, Anlyinmap)
    rule_2(code, Anlyinmap)
    rule_3(code, Anlyinmap)
    rule_4(code, Anlyinmap)
    rule_5(code, Anlyinmap)
    rule_6(code, Anlyinmap)
    rule_7(code, Anlyinmap)
    rule_8(code, Anlyinmap)
    rule_9(code, Anlyinmap)
    rule_10(code, Anlyinmap)
    rule_11(code, Anlyinmap)
    rule_12(code, Anlyinmap)
    #rule_80(code, Anlyinmap)
    #rule_81(code, Anlyinmap)
    
    '''
    rule_82(code, Anlyinmap, 30)
    rule_82(code, Anlyinmap, 20)
    rule_82(code, Anlyinmap, 10)
    rule_82(code, Anlyinmap, 5)
    '''
#end of "def"


#����
def afa_proc_analyse():
    global List_tbl

    if os.path.exists(gl.path_data_origin) <= 0: #�ж�Ŀ���Ƿ����
        os.mkdir(gl.path_data_origin)
    if os.path.exists(gl.path_data_avg) <= 0:    #�ж�Ŀ���Ƿ����
        os.mkdir(gl.path_data_avg)
    if os.path.exists(gl.path_rule_rst) <= 0:    #�ж�Ŀ���Ƿ����
        os.mkdir(gl.path_rule_rst)
    if os.path.exists(gl.path_view_rst) <= 0:    #�ж�Ŀ���Ƿ����
        os.mkdir(gl.path_view_rst)
        
    #1)��ȡ������list������codes�б��п������ݲ�ȫ��  
    get_List_tbl()
    
    #2����list����ȡÿ��tbl�����ݣ�������
    for code in List_tbl:
        gl.STCode = code
        #2.1)��ȡtbl���ݣ�����Anlyinmap      
        flag = acc_tbl_read(code)
        if flag == 1:
            afa_ruleget(code)
            afa_ruleanlys(code)
            print("3:rules������ϣ�")
        else:
            print("3:rules���������ݡ�����")    
    #end for
#endof 'mdl'

#acc_tbl_read('000001')
afa_proc_analyse()
