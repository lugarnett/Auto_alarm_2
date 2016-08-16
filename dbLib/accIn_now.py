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
from accIn_repair import tbl_repair

#模块内全局变量
df = collections.OrderedDict()
List_tbl = []
todaydate = datetime.datetime.now().strftime("%Y-%m-%d")
#todaydate = '2016-07-15'

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
            if tblname.count('MSys') >= 1 or tblname.count('Codes') >= 1:
                continue
            else:
                List_tbl.append(tblname)
        #end for
    except Exception as e:
        print(e)
        print("获取List_tbl出错。。。。。。")
    #print(List_tbl)
#endof 'mdl'

'''2)删除所有tbl中当天日期的数据'''
def foreach_delt_today(delet_date):
    global List_tbl, data
    try:
        for code in List_tbl:
            sql = "DELETE * FROM %s WHERE date = #%s#"%(code, delet_date)
            data.db_del(sql) 
            print("删除%s->%s数据"%(code, delet_date))
        #end for
    except Exception as e:
        print(e)
        print("删除%s当天数据出错。。。。。。"%code)
#endof 'mdl'
    
'''3)获取tushare当天数据'''
def today_tushare_get():
    global df
    
    #获取code，出错则重试10次
    for i in range(10):
        try:
            df = ts.get_today_all()  
            df.sort(['code'], inplace=True)
        except Exception as e:
            print(e)
            print('today_tushare获取失败。。。')
            continue
        #endof 'try'
        break
    #endof 'for'
        
    if df is None:
        print('today_tushare获取失败。。。')
        return -1, None
    else:        
        print('today_tushare获取成功！')
        return 1
    #endof 'if'    
#endof 'mdl'


'''4.1)获取表里的最大ID'''
def get_tbl_maxid(code):
    global data
    try:
        sql = "SELECT MAX(ID) FROM %s"%code
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            maxid = int(a['Expr1000'])
        #end for                    
    except Exception as e:
        print(e)
        maxid = 0

    return maxid
#endof 'mdl'
    
'''4.2)按当前日期，插入数据'''
def today_tushare_insert(code, maxID):
    global df, data, todaydate, List_tbl
    
    try:
        开0 = float(df[df['code']==code]['open'])
        高0 = float(df[df['code']==code]['high'])
        低0 = float(df[df['code']==code]['low'])
        现0 = float(df[df['code']==code]['trade'])
        量0 = float(df[df['code']==code]['volume']) / 100.0
        换0 = float(df[df['code']==code]['turnoverratio']) 
        金额0 = float(df[df['code']==code]['amount'])
                
        per = float(df[df['code']==code]['per'])
        pb = float(df[df['code']==code]['pb'])
        mktcap = float(df[df['code']==code]['mktcap'])
        nmc = float(df[df['code']==code]['nmc'])
                
        '''按当天时间，插入到tbl（此处注意，数据不一定对应当天时间！！！！！）''' 
        '''acc操作'''
        sql = "INSERT INTO [%s] ( \
        [ID],[date], \
        [开1],[高1],[低1],[收1], \
        [开0],[高0],[低0],[收0], \
        [fma5],[fma10],[fma20],[fma30],[fma60],[fma120], \
        [ma5],[ma10],[ma20],[ma30],[ma60],[ma120], \
        [v_ma5],[v_ma10],[v_ma20], \
        [量],[换],[金额],[price_change],[p_change]) \
        VALUES ( \
        '%d','%s', \
        '%f','%f','%f','%f', \
        '%f','%f','%f','%f', \
        '%f','%f','%f','%f','%f','%f', \
        '%f','%f','%f','%f','%f','%f', \
        '%f','%f','%f', \
        '%f','%f','%f','%f','%f')" \
        %(code, \
        maxID+1, todaydate, \
        0, 0, 0, 0, \
        开0, 高0, 低0, 现0, \
        0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, \
        0, 0, 0, \
        量0, 换0, 金额0, 0, 0)        
                
        if(data.db_add(sql)):
            print("%s当日数据已存入"%code)
        else:
            print("%s当日数据已存入失败。。。。。。。"%code)
        #end if
    except Exception as e:
        print(e)            
#endof 'mdl'


'''获取tushare当天最新数据'''
def acc_make3():
    global List_tbl, todaydate
    
    #1)存在的表
    get_List_tbl()

    #2)删除所有tbl中当天日期的数据
    #foreach_delt_today(todaydate)
        
    #3)获取tushare当天数据
    flag = today_tushare_get()
    if flag != 1:
        return
    #endif
    '''存在风险（数据和当前date不一致，导致出现多余日期）（暂不处理，非法数据用完后，按错误日期全部删除）'''
    
    #4)按当前日期，插入数据
    for code in List_tbl:
        maxID = get_tbl_maxid(code) #4.1)
        today_tushare_insert(code, maxID) #4.2)
        tbl_repair(code, 'today') #4.2)
    #end for

#endof 'mdl'

t0 = time.time()
print("\n当前运行模块 -> acc_make3...\n")
if 0:
    acc_make3()
else:
    #5)删除所有tbl中当天日期的数据
    get_List_tbl()
    foreach_delt_today(todaydate)
t1 = time.time()
print("耗时约%d分"%((t1-t0)/60))
