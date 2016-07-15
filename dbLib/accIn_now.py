# -*- coding: utf-8 -*-
import os
import sys
#sys.path.append("\\")
#import gl
import tushare as ts
import datetime
import time
import collections
import json
import win32com.client

from accLib import Access_Model

#模块内全局变量
CodesNet = collections.OrderedDict()
List_tbl = []
todaydate = datetime.datetime.now().strftime("%Y-%m-%d")

dataUrl = os.getcwd()+"\\data.mdb"
data = Access_Model(dataUrl)


'''1)获取List_tbl'''
def get_List_tbl():
    global List_tbl, data
    List_tbl.clear()
    try:
        sql = "SELECT Name FROM MSysObjects Where Type=1 ORDER BY Name"
        dataRecordSet = data.db_query(sql)
        #全部表名，去掉系统表名
        for item in dataRecordSet:
            a = eval("("+item+")")
            tblname = a['Name']
            if tblname.count('MSys') >= 1:
                continue
            else:
                List_tbl.append(tblname)
        #end for
    except Exception as e:
        print(e)
    #print(List_tbl)
#endof 'mdl'

'''2)删除所有tbl中当天日期的数据'''
def foreach_delt_today():
    global List_tbl, data, todaydate
    try:
        for code in List_tbl:
            sql = "DELETE * FROM %s WHERE date = #%s#"%(code, todaydate)
            dataRecordSet = data.db_query(sql)
        #end for
    except Exception as e:
        print(e)
#endof 'mdl'
    
'''3)获取tushare当天数据'''
def today_tushare_get(code):
    global CodesNet, data, todaydate
    
    #获取code，出错则重试10次
    for i in range(10):
        try:
            CodesNet = ts.get_today_all()  
            CodesNet.sort(['code'], inplace=True)
        except Exception as e:
            print(e)
            print('today_tushare获取失败。。。')
            continue
        #endof 'try'
        break
    #endof 'for'
        
    if CodesNet is None:
        print('today_tushare获取失败。。。')
        return -1, None
    else:        
        print('today_tushare获取成功！')
        return 1
    #endof 'if'    
#endof 'mdl'

'''4)按当前日期，插入数据'''
def today_tushare_tbl():
    global CodesNet, data, todaydate
    
    
    #data.conn.open()
    n = 0   
    try:    
        for each in CodesNet.index:
            code = CodesNet.values[n][0]
            if code in List_tbl:
                #名称 = CodesNet.values[n][1]
                #sql = "INSERT INTO Codes([code],[名称]) VALUES ('%s','%s')"%(code, 名称)
                #
                pass
                '''按当天时间，插入到tbl（此处注意，数据不一定对应当天时间！！！！！）'''                
            #end if
                
            #读取数据库历史数据（按时间datetime--）取足够的个数做平均
                
            #更新当前日期行的各均值
                
                
                
            n = n + 1
        #end for 
        #print("Codes表更新完成，共'%d'，新增'%d'"%(n, n_ins))
    
#endof 'mdl'
    


    
    #2.2)获取maxID
    
    #2.3)tushare数据
    
    #2.4)更新基本K
    
    #2.5)删除当天日期的数据
    


'''获取tushare当天最新数据'''
def acc_make3():
    global List_tbl
    
    #1)存在的表
    get_List_tbl()

    #2)删除所有tbl中当天日期的数据
    foreach_delt_today()
        
    #3)获取tushare当天数据
    flag = today_tushare_get()
    if flag != 1:
        return
    #endif
    '''存在风险（数据和当前date不一致，导致出现多余日期）（暂不处理，非法数据用完后，按错误日期全部删除）'''
    
    #4)按当前日期，插入数据
    for code in List_tbl:
        today_tushare_tbl(code)
    #end for

#endof 'mdl'

#print("\n当前运行模块 -> acc_make3...\n")
#acc_make3()
#2)删除所有tbl中当天日期的数据
#foreach_delt_today()
    
    
