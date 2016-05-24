# -*- coding: utf-8 -*-
import gl
from codeGet import mdl_codeget
from calcAvrg import mdl_calcAvrg
from ruleAnalyse import mdl_ruleAnalyse
from mainView import mdl_mainview

import tushare as ts
import os
import collections
import time
#from pandas import Series,DataFrame
#import pandas as pd


#模块内全局变量
flagA = '60'
flagS = '00'
flagFQ = 1
startDate = ''
endDate = ''
DatasrcMap = collections.OrderedDict()

'''通过tushare接口获取数据'''
def get_data():
    global DatasrcMap
    DatasrcMap.clear()
    
    try:
        dataframe = ts.get_h_data(gl.STCode, start=startDate, end=endDate, retry_count=10)  
    except Exception as e:
        print(e)
        time.sleep(1) #网络异常，等待30s
        return -1
        
    if dataframe is None:
        return -1
        
    dataframe.sort_index(inplace=True)  #按date升序排列
    dataframe = dataframe.tail(10+60)  #截取最近20天的数据
    #print(dataframe)
    day = 0
    for each in dataframe.index:
        date = each.strftime('%Y-%m-%d')
        开 = float(dataframe[day:day+1]['open'])
        高 = float(dataframe[day:day+1]['high'])
        低 = float(dataframe[day:day+1]['low'])
        收 = float(dataframe[day:day+1]['close'])
        量 = float(dataframe[day:day+1]['volume']) 
        金额 = float(dataframe[day:day+1]['amount'])                                     
        DatasrcMap[day] = [date,开,高,低,收,量,金额]
        day = day + 1
    #endof 'for' 
    return 1
#endof 'def'

def pro_1by1():
    #1
    flag = get_data()
    if flag == 1:
        print("\n1:data获取成功！")
        #2
        mdl_calcAvrg(DatasrcMap)
        #3
        mdl_ruleAnalyse()
        #4
        mdl_mainview()
    else:
        print("\n1:data获取。。。。。。。。。。。。")
    #endof 'if'
#endof 'def'


'''设置获取数据的参数'''
def mode_selc():
    global startDate,endDate
    
    endDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    startyear = int(endDate[0:4]) - 1 
    startmonth = int(endDate[6:7]) + 8
    if startmonth >= 13:
        startmonth = startmonth % 12
        startyear = startyear + 1
    if startmonth < 10:
        startDate = '%i'%startyear + '-0%i'%startmonth + '-01'
    else:
        startDate = '%i'%startyear + '-%i'%startmonth + '-01'    
#endof 'def'


#main()
mode_selc()

if os.path.exists(gl.path_data_origin) <= 0: #判断目标是否存在
    os.mkdir(gl.path_data_origin)
if os.path.exists(gl.path_data_avg) <= 0:    #判断目标是否存在
    os.mkdir(gl.path_data_avg)
if os.path.exists(gl.path_rule_rst) <= 0:    #判断目标是否存在
    os.mkdir(gl.path_rule_rst)
if os.path.exists(gl.path_view_rst) <= 0:    #判断目标是否存在
    os.mkdir(gl.path_view_rst)
        
gl.STCode = '600167'
print('\n开始处理code='+gl.STCode+'.............')
pro_1by1()

#数据代码范围，遍历
flag, CodeMap = mdl_codeget()
if flag == 1:
    no = 0
    for (n,x) in CodeMap.items():
        no = no + 1        
        gl.STCode = x[0]
        gl.STName = x[1]
        print('\nNo%d -> '%no+gl.STCode+gl.STName+'.............')
        pro_1by1()
    
    #endof 'for'
    print('\n全部计算完毕!')
#endof 'if'
#endof 'main'










