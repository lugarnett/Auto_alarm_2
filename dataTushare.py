# -*- coding: utf-8 -*-
from calcAvrg import mdl_calcAvrg

import gl

import tushare as ts
#import os
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


'''通过tushare接口获取数据'''
def get_data():
    
    dataframe = ts.get_h_data('002337', start=startDate, end=endDate)
    
    day = len(dataframe.index)
    for each in dataframe.index:
        day = day - 1
        if(day >= 0):   
            date = each.strftime('%Y-%m-%d')
            开 = float(dataframe[day:day+1]['open'])
            高 = float(dataframe[day:day+1]['high'])
            低 = float(dataframe[day:day+1]['low'])
            收 = float(dataframe[day:day+1]['close'])
            量 = float(dataframe[day:day+1]['volume']) 
            金额 = float(dataframe[day:day+1]['amount'])                                     
      
            gl.DatasrcMap[day] = [date,开,高,低,收,量,金额]
        #endof 'if'
    #endof 'for'  
#endof 'def'


'''设置获取数据的参数'''
def mode_selc():
    global startDate,endDate
    
    endDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    startyear = int(endDate[0:4]) - 1 
    startmonth = int(endDate[6:7]) + 11
    if startmonth >= 13:
        startmonth = 1
        startyear = startyear + 1
    if startmonth < 10:
        startDate = '%i'%startyear + '-0%i'%startmonth + '-01'
    else:
        startDate = '%i'%startyear + '-%i'%startmonth + '-01'

    #数据代码范围，遍历
    gl.STCode = '002419'
    
#endof 'def'


'''main()'''
#1
mode_selc()
get_data()
#2
mdl_calcAvrg()


#endof 'main()'