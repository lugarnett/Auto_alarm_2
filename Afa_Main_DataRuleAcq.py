# -*- coding: gbk -*-
'''采用acc数据，完成快速分析'''
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

'''1)获取List_tbl'''
def get_List_tbl():
    global List_tbl
    try:
        List_tbl.clear()

        sql = "SELECT Name FROM MSysObjects Where Type=1 ORDER BY Name"
        dataRecordSet = data.db_query(sql)
        #全部表名，去掉系统表名
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
        
'''2.1)读取acc_tbl的交易数据'''
def acc_tbl_read(code):
    global Anlyinmap, Analyse_days
    
    #Outmap.clear()
    Anlyinmap.clear()

    ##研究标的的日期为key
    try:
        #读取row_cnt
        sql = "SELECT COUNT(date) FROM %s"%code
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            row = int(a['Expr1000'])
        #end for
        
        '''根据分析数据条数，算出起止date'''
        startdate = datetime.datetime.now()
        #.strftime("%Y-%m-%d")  
        #print(startdate)
        #startdate = datetime.date(y, m, d)  #str -> datetime
        startdate = startdate + datetime.timedelta(days = -20)  #减n天
        startdate = (startdate.strftime("%Y-%m-%d"))
        #print(startdate)
        
        if row > 0:
            sql = "Select * FROM %s WHERE date>%s ORDER BY date"%(code, startdate) 
            dataRecordSet = data.db_query(sql)
            #Anlyinmap的key为i++序号
            i = 0
            for item in dataRecordSet:
                a = eval("("+item+")")    #eval解析JSON数据
                
                ##############################################################
                #暂时按老数据格式，存入Anlyinmap
                #先按复权数据处理（若需处理无复权数据，可在此替换，或再次调用）
                Anlyinmap[i] = {'date':a['date'][0:10], \
                '基K':[float(a['开1']), float(a['高1']), float(a['低1']), float(a['收1'])], \
                'V':[float(a['量']), float(a['金额']), float(a['p_change'])], \
                'V_ma':[float(a['v_ma5']), float(a['v_ma10']), float(a['v_ma20'])], \
                '换':float(a['换']), \
                '均':[float(a['fma5']), float(a['fma10']), float(a['fma20']), float(a['fma30']), float(a['fma60'])], \
                
                '基K0':[float(a['开0']), float(a['高0']), float(a['低0']), float(a['收0'])], \
                '均0':[float(a['ma5']), float(a['ma10']), float(a['ma20']), float(a['ma30']), float(a['ma60'])]}
                ##############################################################

                #读取其他分析输入数据（如大盘K、消息面），按日期key并入outmap
                
                i = i + 1
                ##分析天数够时，停止读取数据
                if i >= Analyse_days:
                    break
                #end if
            #end for
            print("\n%s表获取成功！"%code)
            #print(Anlyinmap)
            return 1
        else:
            print("\n%s表数据row=0。。。。。"%code)
            return -1
        #end if
    except Exception as e:
        print(e)
        print("\n%s表获取失败。。。。。"%code)
        return -1

#end of "def"


'''2.2)读取rules'''
def afa_ruleget(code):
    global rules
    
    #初步定为采用 字符串数组对应的函数名数组
    
    if 1==1:
        rules.append({'一阳穿五线', 'rule1'})
    if 1==2:
        rules.append({'低开长阳', 'rule2'})
#end of "def"


'''2.3)进行数据分析'''
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


#遍历
def afa_proc_analyse():
    global List_tbl

    if os.path.exists(gl.path_data_origin) <= 0: #判断目标是否存在
        os.mkdir(gl.path_data_origin)
    if os.path.exists(gl.path_data_avg) <= 0:    #判断目标是否存在
        os.mkdir(gl.path_data_avg)
    if os.path.exists(gl.path_rule_rst) <= 0:    #判断目标是否存在
        os.mkdir(gl.path_rule_rst)
    if os.path.exists(gl.path_view_rst) <= 0:    #判断目标是否存在
        os.mkdir(gl.path_view_rst)
        
    #1)获取表名的list（不是codes列表，有可能数据不全）  
    get_List_tbl()
    
    #2遍历list，读取每个tbl的数据，并分析
    for code in List_tbl:
        gl.STCode = code
        #2.1)读取tbl数据，放入Anlyinmap      
        flag = acc_tbl_read(code)
        if flag == 1:
            afa_ruleget(code)
            afa_ruleanlys(code)
            print("3:rules分析完毕！")
        else:
            print("3:rules分析无数据。。。")    
    #end for
#endof 'mdl'

#acc_tbl_read('000001')
afa_proc_analyse()
