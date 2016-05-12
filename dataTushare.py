# -*- coding: utf-8 -*-
import gl
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
    gl.DatasrcMap.clear()
    
    dataframe = ts.get_h_data(gl.STCode, start=startDate, end=endDate)  
    if dataframe is None:
        return -1
        
    dataframe.sort_index(inplace=True)  #按date升序排列
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
        gl.DatasrcMap[day] = [date,开,高,低,收,量,金额]
        day = day + 1
    #endof 'for' 
    #print(gl.DatasrcMap)
    return 1
#endof 'def'


'''设置获取数据的参数'''
def mode_selc():
    global startDate,endDate
    
    endDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    startyear = int(endDate[0:4]) - 1 
    startmonth = int(endDate[6:7]) + 1
    if startmonth >= 13:
        startmonth = startmonth % 12
        startyear = startyear + 1
    if startmonth < 10:
        startDate = '%i'%startyear + '-0%i'%startmonth + '-01'
    else:
        startDate = '%i'%startyear + '-%i'%startmonth + '-01'    
#endof 'def'


def pro_1by1():
    #1
    flag = get_data()
    if flag >= 1:
        #2
        mdl_calcAvrg(DatasrcMap)
        #3
        mdl_ruleAnalyse()
        #4
        mdl_mainview()
    #endof 'if'
#endof 'def'

#main()
mode_selc()
'''
codeframe = ts.get_today_all()
codeframe.sort_index(inplace=True)  #按date升序排列
for each in codeframe.index:
    i = int(each)
    gl.STCode = codeframe[i:i+1]['code']
    print('开始处理code='+gl.STCode+'.............')   
    
    #数据代码范围，遍历'''
for i in range(300000, 300500):     
    if   i < 10:    code = '00000'+'%d'%i
    elif i < 100:   code = '0000' +'%d'%i
    elif i < 1000:  code = '000'  +'%d'%i
    elif i < 10000: code = '00'   +'%d'%i
    elif i < 100000:code = '0'    +'%d'%i
    elif i < 700000:code = '%d'%i
    else :code = '000000'

    gl.STCode = code
    print('\n开始处理code='+gl.STCode+'.............')
    pro_1by1()
    
for i in range(600000, 601000):     
    if   i < 10:    code = '00000'+'%d'%i
    elif i < 100:   code = '0000' +'%d'%i
    elif i < 1000:  code = '000'  +'%d'%i
    elif i < 10000: code = '00'   +'%d'%i
    elif i < 100000:code = '0'    +'%d'%i
    elif i < 700000:code = '%d'%i
    else :code = '000000'
    
    gl.STCode = code
    print('\n开始处理code='+gl.STCode+'.............')
    pro_1by1()
 
#endof 'main'










