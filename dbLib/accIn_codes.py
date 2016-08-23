# -*- coding: utf-8 -*-
import os
#import sys
#sys.path.append("\\")
#import gl
import time
import tushare as ts
#import collections
#import json
#import win32com.client

import accLib

#模块内全局变量
CodesNet = None
List_acc = []
dataUrl = os.getcwd()+"\\data.mdb"
data = accLib.Access_Model(dataUrl)

'''1)codes建表 '''
def codes_tbl_make():
    global data
    try:
        sql = "Create TABLE [Codes] ([code] TEXT,[名称] TEXT, \
                            [沪深] TEXT,[小] TEXT,[创] TEXT,[ST] TEXT, \
                            [市值] FLOAT,[流通市值] FLOAT,[其他] TEXT)"
        data.db_tbl(sql)
    except Exception as e:
        #print(e)
        return
#endof 'mdl'
    
'''2)通过tushare接口获取数据'''
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
        
'''3)获取acc_codes'''
def codesget_acc():
    global List_acc, data
    
    try:
        List_acc.clear()
   
        sql = "SELECT COUNT(code) FROM Codes"
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            row = int(a['Expr1000'])
        #end for
        
        if row > 0:
            sql = "Select code FROM Codes" 
            dataRecordSet = data.db_query(sql)
            #print(dataRecordSet)
            for item in dataRecordSet:
                a = eval("("+item+")")    #eval解析JSON数据
                List_acc.append(a['code'])
            #end for
            print('CodesAcc获取成功！')
        #end if
    except (TypeError,ValueError) as e:
        print("error:"+str(e))
    #print(List_acc)
#endof 'mdl'

'''第一步：codes建表，获取tushare & acc的codes，并比较存储'''
def acc_make1():
    global CodesNet, data
    
    #1)
    codes_tbl_make()
    #2)
    codesget_acc()
    #3)
    flag = codesget_net()
    if flag == -1:
        return -1

    try:
        n = 0
        n_ins = 0
        for each in CodesNet.index:
            code = CodesNet.values[n][0]
            if code in List_acc:
                pass
                ##填充或修改其他值
            else:
                沪深 = '深'
                小 = '-'
                创 = '-'
                ST = '-'
                
                if code[0:1] == '6':
                    沪深 = '沪'
                elif code[0:3] == '002':
                    小 = '小'
                elif code[0:1] == '3':
                    创 = '创'
                
                名称 = CodesNet.values[n][1]
                if 名称.find('ST') > 0:
                    ST = 'ST'
                
                sql = "INSERT INTO Codes([code],[名称],[沪深],[小],[创],[ST]) \
                    VALUES ('%s','%s','%s','%s','%s','%s')"%(code,名称,沪深,小,创,ST)
                data.db_add(sql)
                n_ins = n_ins + 1
            #end if
            n = n + 1
        #end for 
        print("Codes表更新完成，共'%d'，新增'%d'"%(n, n_ins))
    except (TypeError,ValueError) as e:
        print("error:"+str(e))

#endof 'mdl'

print("\n当前运行模块 -> acc_make1...\n")
t0 = time.time()
acc_make1()
t1 = time.time()
print("耗时约%.2f分"%((t1-t0)/60, ))


