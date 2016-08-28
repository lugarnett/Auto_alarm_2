# -*- coding: gbk -*-
'''����acc���ݣ���ɿ��ٷ���'''
import gl
import time

import dbLib.accIn_now
import dbLib.accLib
import dbLib.whlAnly_getRdy

import collections
import os
import datetime

Anlyinmap = collections.OrderedDict()  
Drawinmap = collections.OrderedDict()  
rules = []

List_tbl = []
dataUrl = os.getcwd()+"\\dbLib\\data.mdb"
data = dbLib.accLib.Access_Model(dataUrl)

enddate = datetime.datetime.now()
startdate = datetime.datetime.now()
    
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
    global Anlyinmap, Drawinmap,startdate,enddate
    
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
        str_startdate = startdate.strftime("%Y-%m-%d")
        str_enddate = enddate.strftime("%Y-%m-%d")
        
        if row > 0:
            sql = "Select * FROM %s WHERE date BETWEEN #%s# and #%s# ORDER BY date"%(code,str_startdate,str_enddate) 
            dataRecordSet = data.db_query(sql)
            #Anlyinmap��keyΪi++���
            i = 0
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
                if i >= gl.Analyse_days_date:
                    break
                #end if
            #end for
            #print("%s���ȡ�ɹ���"%code)
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

    ####whlAnly_getRdy.py����
    dbLib.whlAnly_getRdy.whlAnly_1(code, Anlyinmap)
#end of "def"

'''����������ں�������ȡ�����б�����������'''
def afa_proc_analyse():
    global List_tbl, Drawinmap
        
    #1)��ȡ������list������codes�б��п������ݲ�ȫ��  
    get_List_tbl()
    
    ############ List_tbl = ['000001']################################
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
            #afa_ruleget(code)
            afa_ruleanlys(code)
            #afa_mainview(Drawinmap)
            #print("3:rules������ϣ�")
        else:
            print("3:rules���������ݡ�����")    
    #end for
            
    #3��whlAnly��������д��acc
    dbLib.whlAnly_getRdy.update_whlAnlyTbl()        
#endof 'mdl'

def init():
    ####��ʼ��
    gl.������ͣ�� = 0
    gl.����ѡ����= 0
    gl.ZT_1����5�� = 0
    gl.ZT_1����5��N = 0
    gl.ZT_1����5���� = 0.0
    gl.ZT_2����5�� = 0
    gl.ZT_2����5��N = 0
    gl.ZT_2����5���� = 0.0
    gl.ZT_1�����2����5�� = 0
    gl.ZT_1�����2����5��N = 0
    gl.ZT_1�����2����5���� = 0.0
    gl.ZT_1�����3����5�� = 0
    gl.ZT_1�����3����5��N = 0
    gl.ZT_1�����3����5���� = 0.0
    gl.XG_1����5�� = 0
    gl.XG_1����5��N = 0
    gl.XG_1����5���� = 0.0
    gl.XG_2����5�� = 0
    gl.XG_2����5��N = 0
    gl.XG_2����5���� = 0.0
    ####��������ɸѡ
    gl.Date0 = ''
    gl.Cnt_0 = 1
#end def
def IO_tmp_whlAnly_fillAll():
    global startdate,enddate
    
    '''����700�죬���������whlAnly������'''
    for i in range(700):
        init()
        enddate = enddate + datetime.timedelta(days = -1)  #��1��
        startdate = enddate + datetime.timedelta(days = - gl.Analyse_days_date)  #��n��
        
        print("\n��ǰ����ģ�� -> IO_tmp_whlAnly_fillAll��-%d��...\n"%i)
        t0 = time.time()
        afa_proc_analyse()
        t1 = time.time()
        print("\nСģ��%d����ɣ���ʱԼ%.2f��\n"%(i, (t1-t0)/60))
        time.sleep(10)
    #end for
#end def

IO_tmp_whlAnly_fillAll()

