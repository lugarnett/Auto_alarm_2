# -*- coding: utf-8 -*-
import os
from . import accLib


#模块内全局变量
dataUrl = os.getcwd()+"\\dbLib\\data.mdb"
data = accLib.Access_Model(dataUrl)
ID_list = []


'''1.1)找0rows'''
def find_0_cnt(code, flag, m):
    global data

    row = 0
    try:
        sql = "SELECT COUNT(*) FROM %s WHERE %s = 0.0 AND ID >= %d"%(code, flag, m)
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            row = int(a['Expr1000'])
        #end for        
    except Exception as e:
        print(e)
        
    return row
#endof 'mdl'

'''1.2)找0行的ID_list'''
def find_ID_list(code, flag, m):
    global data, ID_list
    
    ID_list.clear()
    try:
        sql = "SELECT ID FROM %s WHERE %s = 0.0 AND ID >= %d ORDER BY ID"%(code, flag, m)
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            b = int(a['ID'])
            ID_list.append(b)
        #end for        
    except Exception as e:
        print(e)    
#endof 'mdl'
    
'''2)读、求均值、更新'''
def ma_read_calc_update(code, flag, m, x):
    global data, ID_list
    
    
    if flag.count('v_ma') >= 1:
        收 = '量'
    elif flag.count('fma') >= 1:
        收 = '收1'
    else:
        收 = '收0'
    #end if

    if x-m+1 < 0: #数据不够
        return
        
    sum收 = 0.0
    try:
        #2.1)读        
        sql = "SELECT %s FROM %s WHERE ID >= %d AND ID <= %d ORDER BY ID"%(收, code, x-m+1, x)
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            b = float(a[收])
            sum收 = sum收 + b
        #end for
        #2.2)求
        avg = sum收 / m
        #2.3)更新
        sql = "UPDATE %s SET %s=%f WHERE ID=%d"%(code, flag, avg, x)
        dataRecordSet = data.db_modi(sql)
    except Exception as e:
        print(e)
#endof 'mdl'
    
'''查找code表中均值为0的行，计算并更新'''
def tbl_repair(code, mode):
    global ID_list
    
    if mode == 'each_tbl':
        flag_list = ['ma5', 'ma10', 'ma20', 'ma30', 'ma60']
    elif mode == 'today':
        flag_list = ['ma5', 'ma10', 'ma20', 'ma30', 'ma60', 'v_ma5', 'v_ma10', 'v_ma20']
    else:
        return
        
    for flag in flag_list:
        
        if flag.count('5') >= 1:
            m = 5
        elif flag.count('10') >= 1:
            m = 10
        elif flag.count('20') >= 1:
            m = 20
        elif flag.count('30') >= 1:
            m = 30
        elif flag.count('60') >= 1:
            m = 60
        else:
            m = 120
        #end if
            
        #1.1)是否有0
        row = find_0_cnt(code, flag, m)
        #print(flag +': ' + str(row)) ##################
        if row > 0:
            #1.2)找0行的ID_list
            find_ID_list(code, flag, m)
        #end if    
            
        #2)遍历ID_list，读、求均值、更新
        for x in ID_list:
            ma_read_calc_update(code, flag, m, x)
        #end for
    #end for
    print("%s表repair完成"%code)
#endof 'mdl'
    
#print("\n当前运行模块 -> tbl_repair...\n")
#tbl_repair('000001')

