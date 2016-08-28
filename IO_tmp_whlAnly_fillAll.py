# -*- coding: gbk -*-
'''采用acc数据，完成快速分析'''
import gl
import time

import dbLib.accIn_now
import dbLib.accLib
import dbLib.whlAnly_getRdy

import collections
import os
import datetime

Anlyinmap = collections.OrderedDict()  
Drawinmap = collections.OrderedDict()  
rules = []

List_tbl = []
dataUrl = os.getcwd()+"\\dbLib\\data.mdb"
data = dbLib.accLib.Access_Model(dataUrl)

enddate = datetime.datetime.now()
startdate = datetime.datetime.now()
    
'''1)获取List_tbl'''
def get_List_tbl():
    global List_tbl
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
            elif tblname.count('0') >= 1 or tblname.count('6') >= 1:
                List_tbl.append(tblname)
        #end for
    except Exception as e:
        print(e)
    #print(List_tbl)
#endof 'mdl'
        
'''2.1)读取acc_tbl的交易数据'''
def acc_tbl_read(code):
    global Anlyinmap, Drawinmap,startdate,enddate
    
    #Outmap.clear()
    Anlyinmap.clear()
    Drawinmap.clear()

    ##研究标的的日期为key
    try:
        #读取row_cnt
        sql = "SELECT COUNT(date) FROM %s"%code
        dataRecordSet = data.db_query(sql)
        for item in dataRecordSet:
            a = eval("("+item+")")
            row = int(a['Expr1000'])
        #end for
        
        '''根据分析数据条数，算出起止date'''
        str_startdate = startdate.strftime("%Y-%m-%d")
        str_enddate = enddate.strftime("%Y-%m-%d")
        
        if row > 0:
            sql = "Select * FROM %s WHERE date BETWEEN #%s# and #%s# ORDER BY date"%(code,str_startdate,str_enddate) 
            dataRecordSet = data.db_query(sql)
            #Anlyinmap的key为i++序号
            i = 0
            for item in dataRecordSet:
                a = eval("("+item+")")    #eval解析JSON数据
                '''
                ##############################################################
                #暂时按老数据格式，存入Anlyinmap
                #先按复权数据处理（若需处理无复权数据，可在此替换，或再次调用）
                Anlyinmap[i] = {'date':a['date'][0:10], \
                '基K':[float(a['开1']), float(a['高1']), float(a['低1']), float(a['收1'])], \
                'V':[float(a['量']), float(a['金额']), float(a['p_change'])], \
                'V_ma':[float(a['v_ma5']), float(a['v_ma10']), float(a['v_ma20'])], \
                '换':float(a['换']), \
                '均':[float(a['fma5']), float(a['fma10']), float(a['fma20']), float(a['fma30']), float(a['fma60'])], \
                
                '基K0':[float(a['开0']), float(a['高0']), float(a['低0']), float(a['收0'])], \
                '均0':[float(a['ma5']), float(a['ma10']), float(a['ma20']), float(a['ma30']), float(a['ma60'])]}
                ##############################################################
                '''
                ##############################################################
                #暂时按老数据格式，存入Anlyinmap
                #先按复权数据处理（若需处理无复权数据，可在此替换，或再次调用）
                Anlyinmap[i] = {'date':a['date'][0:10], \
                '基K':[float(a['开0']), float(a['高0']), float(a['低0']), float(a['收0'])], \
                'V':[float(a['量']), float(a['金额']), float(a['p_change'])], \
                'V_ma':[float(a['v_ma5']), float(a['v_ma10']), float(a['v_ma20'])], \
                '换':float(a['换']), \
                '均':[float(a['ma5']), float(a['ma10']), float(a['ma20']), float(a['ma30']), float(a['ma60'])]}
                ##############################################################
                
                #读取其他分析输入数据（如大盘K、消息面），按日期key并入outmap
                
                i = i + 1
                ##分析天数够时，停止读取数据
                if i >= gl.Analyse_days_date:
                    break
                #end if
            #end for
            #print("%s表获取成功！"%code)
            #print(Anlyinmap)
            
            #数据存入Drawinmap
            for (i,x) in Anlyinmap.items():
                Drawinmap[x['date']] = x
            #end for
            
            return 1
        else:
            print("%s表数据row=0。。。。。"%code)
            return -1
        #end if
    except Exception as e:
        print(e)
        print("%s表获取失败。。。。。"%code)
        return -1

#end of "def"


'''2.2)读取rules'''
def afa_ruleget(code):
    global rules
    
    #初步定为采用 字符串数组对应的函数名数组
    
    if 1==1:
        rules.append({'一阳穿五线', 'rule1'})
    if 1==2:
        rules.append({'低开长阳', 'rule2'})
#end of "def"


'''2.3)进行数据分析'''
def afa_ruleanlys(code):

    ####whlAnly_getRdy.py分析
    dbLib.whlAnly_getRdy.whlAnly_1(code, Anlyinmap)
#end of "def"

'''分析流程入口函数：获取表名列表，并遍历分析'''
def afa_proc_analyse():
    global List_tbl, Drawinmap
        
    #1)获取表名的list（不是codes列表，有可能数据不全）  
    get_List_tbl()
    
    ############ List_tbl = ['000001']################################
    #2遍历list，读取每个tbl的数据，并分析
    sumn = len(List_tbl)
    n = 0
    for code in List_tbl:
        n = n + 1
        print('\n开始处理%s (%d: %d) .............'%(code, sumn, n))
        gl.STCode = code
        #2.1)读取tbl数据，放入Anlyinmap      
        flag = acc_tbl_read(code)
        if flag == 1:
            #afa_ruleget(code)
            afa_ruleanlys(code)
            #afa_mainview(Drawinmap)
            #print("3:rules分析完毕！")
        else:
            print("3:rules分析无数据。。。")    
    #end for
            
    #3将whlAnly分析数据写入acc
    dbLib.whlAnly_getRdy.update_whlAnlyTbl()        
#endof 'mdl'

def init():
    ####初始化
    gl.当天涨停数 = 0
    gl.当天选股数= 0
    gl.ZT_1天涨5数 = 0
    gl.ZT_1天涨5数N = 0
    gl.ZT_1天涨5比例 = 0.0
    gl.ZT_2天涨5数 = 0
    gl.ZT_2天涨5数N = 0
    gl.ZT_2天涨5比例 = 0.0
    gl.ZT_1天买进2天涨5数 = 0
    gl.ZT_1天买进2天涨5数N = 0
    gl.ZT_1天买进2天涨5比例 = 0.0
    gl.ZT_1天买进3天涨5数 = 0
    gl.ZT_1天买进3天涨5数N = 0
    gl.ZT_1天买进3天涨5比例 = 0.0
    gl.XG_1天涨5数 = 0
    gl.XG_1天涨5数N = 0
    gl.XG_1天涨5比例 = 0.0
    gl.XG_2天涨5数 = 0
    gl.XG_2天涨5数N = 0
    gl.XG_2天涨5比例 = 0.0
    ####用于日期筛选
    gl.Date0 = ''
    gl.Cnt_0 = 1
#end def
def IO_tmp_whlAnly_fillAll():
    global startdate,enddate
    
    '''上溯700天，处理两年的whlAnly！！！'''
    for i in range(700):
        init()
        enddate = enddate + datetime.timedelta(days = -1)  #减1天
        startdate = enddate + datetime.timedelta(days = - gl.Analyse_days_date)  #减n天
        
        print("\n当前运行模块 -> IO_tmp_whlAnly_fillAll（-%d）...\n"%i)
        t0 = time.time()
        afa_proc_analyse()
        t1 = time.time()
        print("\n小模块%d已完成，耗时约%.2f分\n"%(i, (t1-t0)/60))
        time.sleep(10)
    #end for
#end def

IO_tmp_whlAnly_fillAll()

