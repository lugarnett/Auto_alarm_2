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
CodesNet = None
List_tbl = []
dataUrl = os.getcwd()+"\\data.mdb"
data = Access_Model(dataUrl)


'''1)获取List_tbl'''
def get_List_tbl():
    global List_tbl, data
    
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
            else:
                List_tbl.append(tblname)
        #end for
    except Exception as e:
        print(e)
    #print(List_tbl)
#endof 'mdl'

'''2)获取tushare当天数据'''
def codesget_net():
    global CodesNet
    
    #获取code，出错则重试10次
    for i in range(10):
        try:
            CodesNet = ts.get_today_all()  
            CodesNet.sort(['code'], inplace=True)
        except Exception as e:
            print(e)
            print('CodesNet获取失败。。。')
            continue
        #endof 'try'
        break
    #endof 'for'
    if CodesNet is None:
        print('CodesNet获取失败。。。')
        return -1, None
    else:        
        print('CodesNet获取成功！')
        return 1
    #endof 'if'    
#endof 'mdl'

'''3)获取tushare当天数据'''
def insert_todaydata():
    global CodesNet, List_tbl
    
    
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
    
'''4)删除各表内的当天数据'''
def delete_todaydata():
    global List_tbl
        
    #data.conn.open()  
    try:    
        for each in List_tbl:
                #名称 = CodesNet.values[n][1]
                #sql = "delete INTO Codes([code],[名称]) VALUES ('%s','%s')"%(code, 名称)
                #

        #end for 
        #print("Codes表更新完成，共'%d'，新增'%d'"%(n, n_ins))
    
#endof 'mdl'

'''第三步：获取当天最新数据，并插入存储，用于计算，计算完成后，删除当天数据'''
def acc_make3():
    global List_tbl
    
    #1)存在的表
    get_List_tbl()

    #2)获取tushare当天数据'''
    codesget_net()
    
    #3)比较，并读取datafram数据，然后插入存储
    insert_todaydata()

    #4)删除当前日期对应的所有表内数据
    #
#endof 'mdl'

print("\n当前运行模块 -> acc_make3...\n")

acc_make3()

#delete_todaydata()
    
    
