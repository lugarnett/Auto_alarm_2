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


#默认的tushare取数起始日期
MAXDATE = '2015-01-01'
maxID = 0


#模块内全局变量
CodesNet = None
List_code = []
List_tbl = []
dataUrl = os.getcwd()+"\\data.mdb"
data = Access_Model(dataUrl)


'''1)获取List_code'''
def get_List_code():
    global List_code, data
    
    try:
        List_code.clear()
   
        sql = "Select code FROM Codes" 
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")    #eval解析JSON数据
            List_code.append(a['code'])
        #end for        
        print('CodesAcc获取成功！')
    except Exception as e:
        print('CodesAcc获取失败。。。。。。。。。。。。。。。。')
        print(e)

    if len(List_code) == 0:
        return -1
    else:
        return 1
#endof 'mdl'

'''2)获取List_tbl'''
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
            if tblname.count('MSys') >= 1 or tblname.count('Codes') >= 1:
                continue
            else:
                List_tbl.append(tblname)
        #end for
        print('TblAcc获取成功！')        
    except Exception as e:
        print('TblAcc获取失败。。。。。。。。。。。。。。。。')
        print(e)
    #print(List_tbl)
#endof 'mdl'
        
'''3.1)建表'''
def tbl_make(code):
    global data
    try:
        sql = "Create TABLE [%s] (\
        [ID] INT PRIMARY KEY, [date] DATE, \
        [开1] FLOAT,[高1] FLOAT,[低1] FLOAT,[收1] FLOAT, \
        [开0] FLOAT,[高0] FLOAT,[低0] FLOAT,[收0] FLOAT, \
        [fma5] FLOAT,[fma10] FLOAT,[fma20] FLOAT,[fma30] FLOAT,[fma60] FLOAT,[fma120] FLOAT, \
        [ma5] FLOAT,[ma10] FLOAT,[ma20] FLOAT,[ma30] FLOAT,[ma60] FLOAT,[ma120] FLOAT, \
        [v_ma5] FLOAT,[v_ma10] FLOAT,[v_ma20] FLOAT,[v_ma30] FLOAT,[v_ma60] FLOAT, \
        [量] FLOAT,[换] FLOAT,[金额] FLOAT, \
        [price_change] FLOAT,[p_change] FLOAT,[信息] TEXT,[备注] TEXT)"%(code)
        data.db_tbl(sql)
    except Exception as e:
        print(e)
#endof 'mdl'


'''3.2.1)获取表里的最新日期'''
def get_tbl_date(code):
    global data
    try:
        sql = "SELECT MAX(date) FROM %s"%code
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            maxdate = a['Expr1000']
        #end for                    
    except Exception as e:
        print(e)
        maxdate = 0

    return maxdate
#endof 'mdl'



'''3.2.2)获取表里的最大ID'''
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
    
'''3.2.3)获取tushare数据(复&不复合二为一)，并写入acc_tbl'''
def get_tushare_tblfill(code, startdate):
    global maxID
    
    if startdate >= datetime.datetime.now().date():
        print("为最新日期数据，无需更新！")
        return -1   
    startDate = startdate.strftime("%Y-%m-%d")  
    endDate = datetime.datetime.now().strftime("%Y-%m-%d")  
    
    print("tushare取数")
    try:
        df0 = ts.get_hist_data(code, start=startDate, end=endDate)  #不复, retry_count=10
        df1 = ts.get_h_data(code, start=startDate, end=endDate)     #复, retry_count=10
    except Exception as e:
        print(e)
        print('sleep。。。。。。。。。。。。。。。。。')
        time.sleep(1) #网络异常，等待30s
        return -1
        
    if df0 is None or df1 is None:
        print('\nNone。。。。。。。。。。。。。。。。。。。。')
        return -1
    #print('\n0:tushare获取成功')
    
    '''排序1'''
    df0.sort_index(inplace=True)  #按date升序排列
    df1.sort_index(inplace=True)  #按date升序排列
    
    '''两个dataframe中不匹配的数据drop'''
    #1)    
    ##df1的类型是datetime，df0的类型是date_str 
    for each in df0.index:
        if each not in df1.index:
            print("df0.drop(%s)"%each)            
            df0.drop(each, inplace=True)
        #end if
    #end for
    print("len(原始)'=%d ： 'len(复)'=%d"%(len(df0), len(df1)))
    #2)
    for each in df1.index:
        if str(each.date()) not in df0.index:     
            print("df1.drop(%s)"%str(each.date())) 
            df1.drop(each, inplace=True)
        #end if
    #end for
    print("len(原始)'=%d ： 'len(复)'=%d"%(len(df0), len(df1)))
    #3)    
    for each in df0.index:
        if each not in df1.index:
            print("df0.drop(%s)"%each)            
            df0.drop(each, inplace=True)
        #end if
    #end for
    print("len(原始)'=%d ： 'len(复)'=%d"%(len(df0), len(df1)))
    
    '''排序2'''
    df0.sort_index(inplace=True)  #按date升序排列
    df1.sort_index(inplace=True)  #按date升序排列
    #print(df0)
    #print(df1)
    if not (len(df0) == len(df1)):
        print("两数据包不匹配...................................")
        print("len(原始)'=%d ： 'len(复)'=%d"%(len(df0), len(df1)))
        return -1
    #end if    
    
    try:
        #数据按date，存入acc
        conn = data.db_conn()
        #dateframe1数据偶尔少1，故以dataframe1为基准
        n = 0 #dateframe的行数
        for each in df1.index:
            date = df1.index[n]
            #print(date)
            #复
            开1 = float(df1[df1.index==date]['open'])
            高1 = float(df1[df1.index==date]['high'])
            低1 = float(df1[df1.index==date]['low'])
            收1 = float(df1[df1.index==date]['close'])
            #量1 = float(df1[df1.index==date]['volume']) 
            金额 = float(df1[df1.index==date]['amount']) 

            #不复
            date2str = str(date.date())    ##df1的类型是datetime，df0的类型是date_str
            开0 = float(df0[df0.index==date2str]['open']) 
            高0 = float(df0[df0.index==date2str]['high'])
            低0 = float(df0[df0.index==date2str]['low'])
            收0 = float(df0[df0.index==date2str]['close'])
            量  = float(df0[df0.index==date2str]['volume']) 
            换  = float(df0[df0.index==date2str]['turnover']) 
            v_ma5  = float(df0[df0.index==date2str]['v_ma5']) 
            v_ma10 = float(df0[df0.index==date2str]['v_ma10']) 
            v_ma20 = float(df0[df0.index==date2str]['v_ma20']) 
            price_change = float(df0[df0.index==date2str]['price_change']) 
            p_change = float(df0[df0.index==date2str]['p_change']) 

            fma5 = 0.0
            fma10 = 0.0
            fma20 = 0.0
            fma30 = 0.0
            fma60 = 0.0
            fma120 = 0.0
            ma5 = 0.0
            ma10 = 0.0
            ma20 = 0.0
            ma30 = 0.0
            ma60 = 0.0
            ma120 = 0.0
            
            #if n == 4:
            if n >= 4:
                for x in range(n-4, n+1):
                    #print('x')
                    #print()
                    收1 = float(df1[x:x+1]['close'])                    
                    fma5 = fma5 + 收1 / 5
                    收0 = float(df0[x:x+1]['close'])
                    ma5 = ma5 + 收0 / 5
                #end for
            #end if
            if n >= 9:
                for x in range(n-9, n+1):
                    收1 = float(df1[x:x+1]['close'])
                    fma10 = fma10 + 收1 / 10
                    收0 = float(df0[x:x+1]['close'])
                    ma10 = ma10 + 收0 / 10
                #end for
            #end if
            if n >= 19:
                for x in range(n-19, n+1):
                    收1 = float(df1[x:x+1]['close'])
                    fma20 = fma20 + 收1 / 20
                    收0 = float(df0[x:x+1]['close'])
                    ma20 = ma20 + 收0 / 20
                #end for
            #end if
            if n >= 29:
                for x in range(n-29, n+1):
                    收1 = float(df1[x:x+1]['close'])
                    fma30 = fma30 + 收1 / 30
                    收0 = float(df0[x:x+1]['close'])
                    ma30 = ma30 + 收0 / 30
                #end for
            #end if
            if n >= 59:
                for x in range(n-59, n+1):
                    收1 = float(df1[x:x+1]['close'])
                    fma60 = fma60 + 收1 / 60
                    收0 = float(df0[x:x+1]['close'])
                    ma60 = ma60 + 收0 / 60
                #end for
            #end if
            '''if n >= 119:
                for x in range(n-119, n+1):
                    收1 = float(df1[x:x+1]['close'])
                    fma120 = fma120 + 收1 / 120
                    收0 = float(df0[x:x+1]['close'])
                    ma120 = ma120 + 收0 / 120
                #end for
            #end if'''
              
            n = n + 1
            maxID = maxID + 1
            
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
            maxID, date2str, \
            开1, 高1, 低1, 收1, \
            开0, 高0, 低0, 收0, \
            fma5, fma10, fma20, fma30, fma60, fma120, \
            ma5, ma10, ma20, ma30, ma60, ma120, \
            v_ma5, v_ma10, v_ma20, \
            量, 换, 金额, price_change, p_change)        

            conn.execute(sql);
        #endof 'for' 
        conn.Close()
        print("%s表更新完成!\n"%code)
        return 1
    except Exception as e:
        print(e)
        conn.Close()
        return -1  
#endof mdl

'''3.2)填表'''
def tbl_fill(code):
    global data, maxID
    try:
        sql = "SELECT COUNT(*) FROM %s"%code
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            row = int(a['Expr1000'])
        #end for

        #1)确定数据时间段
        if row == 0:
            maxdate = MAXDATE    #'2016-01-01'
            maxID = 0
        else:
            #3.2.1)
            maxdate = get_tbl_date(code)
            #3.2.2)
            maxID = get_tbl_maxid(code)
        #end if
        y = int(maxdate[0:4])
        m = int(maxdate[5:7])
        d = int(maxdate[8:10])
        startdate = datetime.date(y, m, d)  #str -> datetime
        startdate = startdate + datetime.timedelta(days = 1)  #加1天

        #2)取时间段内数据，并填入表
        #3.2.3)
        ret = get_tushare_tblfill(code, startdate)

    except Exception as e:
        print(e)
    return ret
#endof 'mdl'

'''第二步：获取codes_acc列表 & 存在的表each，比较，并读取数据，然后建表存储或追加存储'''
def acc_make2():
    global List_code, List_tbl
    
    #1)codes_acc列表
    flag = get_List_code()
    if flag == -1:
        return -1
        
    #2)存在的表
    get_List_tbl()

    #3)比较，并读取数据，然后建表存储或追加存储
    n = 0
    n_new = 0
    sumn = len(List_code)
    for code in List_code:
        if code not in List_tbl:
            tbl_make(code)      #新建表和字段
            n_new = n_new + 1
        #end if        
        n = n + 1
        print('\n开始处理%s (%d: %d) .............'%(code, sumn, n))
        ret = tbl_fill(code)
        #查找均值为0的，计算并存入
        if ret == 1:
            tbl_repair(code, 'each_tbl')
    #end for 
    print("表fill完成，共'%d'，新增'%d'"%(sumn, n_new))


#endof 'mdl'
print("\n当前运行模块 -> acc_make2...\n")
acc_make2()



