# -*- coding: utf-8 -*-
import os
import gl
import collections

from . import accLib

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()
anlyn = 'whlAnly1'
Anly_days = gl.whlAnly_1

#模块内全局变量
CodesNet = None
List_acc = []
dataUrl = os.getcwd()+"\\dbLib\\data.mdb"
data = accLib.Access_Model(dataUrl)
                     
                          
def update_whlAnlyTbl():
    global data
    
    if (gl.ZT_1天涨5数 + gl.ZT_1天涨5数N) == 0:
        gl.ZT_1天涨5比例 = 0.0
    else:        
        gl.ZT_1天涨5比例 = float(gl.ZT_1天涨5数) / (gl.ZT_1天涨5数 + gl.ZT_1天涨5数N)
        
    if (gl.ZT_2天涨5数 + gl.ZT_2天涨5数N) == 0:
        gl.ZT_2天涨5比例 = 0.0
    else:         
        gl.ZT_2天涨5比例 = float(gl.ZT_2天涨5数) / (gl.ZT_2天涨5数 + gl.ZT_2天涨5数N)
    
    if (gl.ZT_1天买进2天涨5数 + gl.ZT_1天买进2天涨5数N) == 0:
        gl.ZT_1天买进2天涨5比例 = 0.0
    else:         
        gl.ZT_1天买进2天涨5比例 = float(gl.ZT_1天买进2天涨5数) / (gl.ZT_1天买进2天涨5数 + gl.ZT_1天买进2天涨5数N)
    
    if (gl.ZT_1天买进3天涨5数 + gl.ZT_1天买进3天涨5数N) == 0:
        gl.ZT_1天买进3天涨5比例 = 0.0
    else:     
        gl.ZT_1天买进3天涨5比例 = float(gl.ZT_1天买进3天涨5数) / (gl.ZT_1天买进3天涨5数 + gl.ZT_1天买进3天涨5数N)
   
    try: 
        #读取row_cnt
        sql = "SELECT COUNT(date) FROM whlAnly WHERE date = #%s#"%(gl.Date0)
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            row = int(a['Expr1000'])
        #end for
        
        if row >= 1:
            sql = "UPDATE whlAnly SET 当天涨停数='%d', 当天选股数='%d', \
                                      ZT_1天涨5数='%d', ZT_1天涨5比例='%.1f', \
                                      ZT_2天涨5数='%d', ZT_2天涨5比例='%.1f', \
                                      ZT_1天买进2天涨5数='%d', ZT_1天买进2天涨5比例='%.1f', \
                                      ZT_1天买进3天涨5数='%d', ZT_1天买进3天涨5比例='%.1f' \
                                      WHERE date = #%s#"%(gl.当天涨停数, gl.当天选股数,
                                    gl.ZT_1天涨5数, gl.ZT_1天涨5比例, 
                                    gl.ZT_2天涨5数, gl.ZT_2天涨5比例, 
                                    gl.ZT_1天买进2天涨5数, gl.ZT_1天买进2天涨5比例, 
                                    gl.ZT_1天买进3天涨5数, gl.ZT_1天买进3天涨5比例, 
                                    gl.Date0)
            data.db_modi(sql)
        else:
            sql = "INSERT INTO whlAnly([date],[当天涨停数],[当天选股数],\
                    [ZT_1天涨5数],[ZT_1天涨5比例],[ZT_2天涨5数],[ZT_2天涨5比例],\
                    [ZT_1天买进2天涨5数],[ZT_1天买进2天涨5比例],[ZT_1天买进3天涨5数],[ZT_1天买进3天涨5比例]) \
                    VALUES ('%s','%d','%d','%d','%.1f','%d','%.1f','%d','%.1f','%d','%.1f'\
                    )"%(gl.Date0, gl.当天涨停数, gl.当天选股数,
                                    gl.ZT_1天涨5数, gl.ZT_1天涨5比例, 
                                    gl.ZT_2天涨5数, gl.ZT_2天涨5比例, 
                                    gl.ZT_1天买进2天涨5数, gl.ZT_1天买进2天涨5比例, 
                                    gl.ZT_1天买进3天涨5数, gl.ZT_1天买进3天涨5比例)
            data.db_add(sql)
        #end if
        print('\nwhlAnlyTbl当日数据已录入acc\n')
    except Exception as e:        
        print(e)

#end def
    
'''涨停数，2天、3天内涨5的统计'''
def whlAnly_1(code, Anlyinmap):
    global Anlyoutmap,Anlymdymap,anlyn,Anly_days

    max_n = max(Anlyinmap.keys())
    days = Anly_days
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
           
    涨停度 = 1.1
    上涨度 = 1.05
    Anlyoutmap.clear()
    
    for (d,x) in Anlymdymap.items():
        if d <= 3:
            continue
        elif d == 4:
            '''一个code只执行一次'''
            xpre4 = Anlymdymap[d-4]
            xpre3 = Anlymdymap[d-3]
            xpre2 = Anlymdymap[d-2]
            xpre1 = Anlymdymap[d-1]

            开pre4 = xpre4['基K'][0]
            高pre4 = xpre4['基K'][1]
            低pre4 = xpre4['基K'][2]
            收pre4 = xpre4['基K'][3]
            
            开pre3 = xpre3['基K'][0]
            高pre3 = xpre3['基K'][1]
            低pre3 = xpre3['基K'][2]
            收pre3 = xpre3['基K'][3]
            
            开pre2 = xpre2['基K'][0]
            高pre2 = xpre2['基K'][1]
            低pre2 = xpre2['基K'][2]
            收pre2 = xpre2['基K'][3]
            
            开pre1 = xpre1['基K'][0]
            高pre1 = xpre1['基K'][1]
            低pre1 = xpre1['基K'][2]
            收pre1 = xpre1['基K'][3]
            
            开 = x['基K'][0]
            高 = x['基K'][1]
            低 = x['基K'][2]
            收 = x['基K'][3]

            #当日涨停（非一字涨停）
            if 收 >= round(涨停度*收pre1, 2) and 开 < 收:
                gl.当天涨停数 = gl.当天涨停数 + 1

            #ZT_1天涨5数:
            if 收pre1 >= round(涨停度*收pre2, 2) and 开pre1 < 收pre1:
                if 高 > 上涨度*收pre1:
                    gl.ZT_1天涨5数 = gl.ZT_1天涨5数 + 1
                else:
                    gl.ZT_1天涨5数N = gl.ZT_1天涨5数N + 1
            
            #ZT_2天涨5数:
            if 收pre2 >= round(涨停度*收pre3, 2) and 开pre2 < 收pre2:
                if (高 > 上涨度*收pre2) or (高pre1 > 上涨度*收pre2):
                    gl.ZT_2天涨5数 = gl.ZT_2天涨5数 + 1
                else:
                    gl.ZT_2天涨5数N = gl.ZT_2天涨5数N + 1
                
            #ZT_1天买进2天涨5数:
            if 收pre2 >= round(涨停度*收pre3, 2) and 开pre2 < 收pre2:
                if 高 > 上涨度*开pre1:
                    gl.ZT_1天买进2天涨5数 = gl.ZT_1天买进2天涨5数 + 1
                else:
                    gl.ZT_1天买进2天涨5数N = gl.ZT_1天买进2天涨5数N + 1   
            
            #ZT_1天买进3天涨5数:
            if 收pre3 >= round(涨停度*收pre4, 2) and 开pre3 < 收pre3:
                if (高pre1 > 上涨度*开pre2) or (高 > 上涨度*开pre2):
                    gl.ZT_1天买进3天涨5数 = gl.ZT_1天买进3天涨5数 + 1
                else:
                    gl.ZT_1天买进3天涨5数N = gl.ZT_1天买进3天涨5数N + 1   
                               
            #当天选股数= 0
            #XG_1天涨5数 = 0
            #XG_1天涨5比例 = 0.0
            #XG_2天涨5数 = 0
            #XG_2天涨5比例 = 0.0
            
            ####用于日期筛选，智能获取当前日期
            if gl.Date0 == x['date']:
                gl.Cnt_0 = gl.Cnt_0 + 1
            else:
                gl.Cnt_0 = gl.Cnt_0 - 1
                if gl.Cnt_0 <= 0:
                    gl.Date0 = x['date']
                #end if
            #end if     
            
    #end of "for"
    
#end of "def"


