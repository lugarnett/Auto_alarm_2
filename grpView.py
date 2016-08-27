# -*- coding: gbk -*-
import gl

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections  
#from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

def gettime():
    return time.strftime("%Y%m%d_%H:%M",time.localtime(time.time()))
def getdate(): 
    return time.strftime('%Y%m%d',time.localtime(time.time()))
    
tmpmap = collections.OrderedDict()
submap = collections.OrderedDict()

日期list=[]
#个股Klist=[]
总手list=[]
金额list=[]
换手list=[]
均5list =[]
均10list=[]
均20list=[]
均30list=[]
均60list=[]

最高list=[]
最低list=[]
        
cnt_rule_pic = 0
xstep = 0.5
offset = (xstep - 0.1) / 2
换trans = 20

def sub_view(submap, code):
    global 日期list,总手list,金额list,换手list,\
            均5list,均10list,均20list,均30list,均60list
    global cnt_rule_pic
     
    日期list.clear()
    总手list.clear()
    金额list.clear()
    换手list.clear()
    均5list .clear()
    均10list.clear()
    均20list.clear()
    均30list.clear()
    均60list.clear()
    
    最高list.clear()
    最低list.clear()
    
    for (d,x) in submap.items():
        日期list.append(d)
        总手list.append(x["V"][0])
        金额list.append(x["V"][1])
        换手list.append(x["V"][2])
        均5list.append(x["均"][0])
        均10list.append(x["均"][1])
        均20list.append(x["均"][2])
        均30list.append(x["均"][3])
        均60list.append(x["均"][4])
        
        最高list.append(x['基K'][1])
        最低list.append(x['基K'][2])
    #end of "for"
        
    xpos = np.arange(0, len(日期list)*xstep, xstep)
    xoffset= xpos + offset
    
    #####fig, ax = plt.subplots()   
    fig = plt.figure(3)                      # Create a `figure' instance
    ax = fig.add_subplot(111)  
    #ax2 = fig.add_subplot(311) 
    #ax3 = fig.add_subplot(312) 
    # 设置图的底边距
    fig.subplots_adjust(bottom = 0.15)
    fig.subplots_adjust(top = 0.8)
    #fig.subplots_adjust(right = 10)
    #fig.subplots_adjust(left = 0.05)
    #fig.grid() #开启网格
    ax.set_xticks(xpos)
    ax.set_xticklabels(日期list, rotation=90, fontsize=6)
    ax.plot(xoffset, 均5list,  '.-', alpha = 0.5, color ='y')
    ax.plot(xoffset, 均10list, '-', alpha = 0.5, color ='yellowgreen')
    ax.plot(xoffset, 均20list, '-', alpha = 0.5, color ='lightskyblue')
    ax.plot(xoffset, 均30list, '-', alpha = 0.5, color ='c')
    ax.plot(xoffset, 均60list, '-', alpha = 0.5, color ='m')
    
    i = 0
    for (d, x) in submap.items():
        日期 = d
        开盘 = x['基K'][0]
        最高 = x['基K'][1]
        最低 = x['基K'][2]
        收盘 = x['基K'][3]
        换 = x['换'] 
        量 = x['V']
        V_ma5 = x['V_ma'][0]
        V_ma10= x['V_ma'][1]
        V_ma20 = x['V_ma'][2]
        
        if 收盘 > 开盘:
            ax.bar(xpos[i], 收盘-开盘, bottom = 开盘, width = .4, alpha = .5, facecolor ='r', edgecolor='r',linewidth=0.5)
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .5, facecolor ='r', edgecolor='r',linewidth=0.5)
        elif 开盘 > 收盘:
            ax.bar(xpos[i], 开盘-收盘, bottom = 收盘, width = .4, alpha = .5, facecolor ='green', edgecolor='green',linewidth=0.5)
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .5, facecolor ='green', edgecolor='green',linewidth=0.5)
        else: #开盘==收盘:
            ax.bar(xpos[i], 0.005, bottom = 开盘, width = .4, alpha = .5, facecolor ='r', edgecolor='r',linewidth=0.5)
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .5, facecolor ='r', edgecolor='r',linewidth=0.5) 
        #end of "if"

        换btm = min(最低list) * 0.9
        ax.bar(xpos[i], 20/换trans, bottom = 换btm, width = .4, alpha = .02, facecolor ='black', edgecolor='black',linewidth=0.5)
        ax.bar(xpos[i], 10/换trans, bottom = 换btm, width = .4, alpha = .025, facecolor ='black', edgecolor='black',linewidth=0.5)
        ax.bar(xpos[i], 5/换trans, bottom = 换btm, width = .4, alpha = .03, facecolor ='black', edgecolor='black',linewidth=0.5)
        ax.bar(xpos[i], 2/换trans, bottom = 换btm, width = .4, alpha = .05, facecolor ='black', edgecolor='black',linewidth=0.5)
        
        换 = 换 / 换trans
        if 收盘 > 开盘:
            ax.bar(xpos[i], 换, bottom = 换btm, width = .4, alpha = .3, facecolor ='r', edgecolor='r',linewidth=0.5)
        else:
            ax.bar(xpos[i], 换, bottom = 换btm, width = .4, alpha = .3, facecolor ='green', edgecolor='green',linewidth=0.5)
        
            

        if  '分析结果' in x:
            结果cnt = 0
            #画矩形
            #squal_x = [xpos[i], xpos[i], xpos[i] + xstep*10]
            #squal_y = [开盘, 开盘*1.2, 开盘*1.2]
            squal_x = [xoffset[i], xoffset[i]]
            squal_y = [收盘, 收盘*1.12]
            ax.plot(squal_x, squal_y, '--', alpha = 0.7, color = 'm', linewidth=0.2)
            for (d2, x2) in x['分析结果'].items():
                #print(日期, d2, x2)
                ruleID = d2[4:]
                if not ruleID=='0':
                    #写文字
                    ax.text(xpos[i], 收盘*1.093+结果cnt*0.015*收盘, d2+' '+x2, alpha = 0.7, color = 'r', fontsize = 6)
                    #ruleID
                    ax.text(xpos[i], 收盘*1.087-结果cnt*0.015*收盘, '('+ruleID+')', color = 'g', fontsize = 6)
                    结果cnt = 结果cnt + 1
                #endof 'if'
            #end of "for"
        #end of "if"       
        i = i + 1
    #endof 'for'
            
    #if os.path.exists(gl.path_view_rst+code) <= 0:    #判断目标是否存在
    #    os.mkdir(gl.path_view_rst+code)
    cnt_rule_pic = cnt_rule_pic + 1
    fig.savefig(gl.path_view_rst+code+'_告警_%d_'%cnt_rule_pic+日期+'.png', dpi = 200)

    fig.clear()
    ax.clear()
    #ax2.clear()
    #ax3.clear()
    del fig
    del ax
    #del ax2
    #del ax3
    #plt.show() 
#end of "def"



def rules_group_find(tmpmap, d):
    
    flag = 0
    #####################################################分类整理
    #####################################################形态3个一般 flag=1
    cnt = len(tmpmap[d][1]['分析结果'])
    if cnt>=3:
        flag = 1
    #####################################################大形态重要 flag=8
    ####专用策略：空中加油        
    if  'rule50' in tmpmap[d][1]['分析结果']:
        flag = 8   
    if  'rule51' in tmpmap[d][1]['分析结果']:
        flag = 8       
    if  'rule52' in tmpmap[d][1]['分析结果']:
        flag = 8     
    if  'rule53' in tmpmap[d][1]['分析结果']:
        flag = 8   
    if  'rule54' in tmpmap[d][1]['分析结果']:
        flag = 8   
    
    ####组合策略        
    if  'rule70' in tmpmap[d][1]['分析结果']:
        flag = 8    
        
    if  'rule80' in tmpmap[d][1]['分析结果']:
        flag = 8    
    if  'rule81' in tmpmap[d][1]['分析结果']:
        flag = 8   
    if  'rule82' in tmpmap[d][1]['分析结果']:
        flag = 8   

    #####################################################大形态一般 flag=7
    if  'rule60' in tmpmap[d][1]['分析结果']:
        flag = 7    
    if  'rule61' in tmpmap[d][1]['分析结果']:
        flag = 7   
    if  'rule62' in tmpmap[d][1]['分析结果']:
        flag = 7    
    if  'rule63' in tmpmap[d][1]['分析结果']:
        flag = 7   
    if  'rule64' in tmpmap[d][1]['分析结果']:
        flag = 7 
    if  'rule65' in tmpmap[d][1]['分析结果']:
        flag = 7 
    #####################################################基本形态重要 flag=6
    
    #####################################################基本形态一般 flag=5
    ####基本（单个）
    if  'rule2' in tmpmap[d][1]['分析结果']:
        flag = 5
    if  'rule3' in tmpmap[d][1]['分析结果']:
        flag = 5 
    if  'rule5' in tmpmap[d][1]['分析结果']:
        flag = 5
    if  'rule7' in tmpmap[d][1]['分析结果']:
        flag = 5
    if  'rule8' in tmpmap[d][1]['分析结果']:
        flag = 5
    if  'rule12' in tmpmap[d][1]['分析结果']:
        flag = 5
    if  'rule13' in tmpmap[d][1]['分析结果']:
        flag = 5
    if  'rule14' in tmpmap[d][1]['分析结果']:
        flag = 5
    if  'rule15' in tmpmap[d][1]['分析结果']:
        flag = 5
    if  'rule17' in tmpmap[d][1]['分析结果']:
        flag = 5
        
    ####基本 + 当日涨停（重要条件）
    if  'rule121' in tmpmap[d][1]['分析结果']:
        if  'rule1' in tmpmap[d][1]['分析结果']:
            flag = 5
        if  'rule4' in tmpmap[d][1]['分析结果']:
            flag = 5
        if  'rule6' in tmpmap[d][1]['分析结果']:
            flag = 5
        if  'rule9' in tmpmap[d][1]['分析结果']:
            flag = 5
        if  'rule11' in tmpmap[d][1]['分析结果']:
            flag = 5
        if  'rule16' in tmpmap[d][1]['分析结果']:
            flag = 5    
        if  'rule18' in tmpmap[d][1]['分析结果']:
            flag = 5
        if  'rule19' in tmpmap[d][1]['分析结果']:
            flag = 5
        #end if
    #end if
    #####################################################        
    return flag, cnt    
#endof 'def'


def sub_grpview_mng(code):
    global tmpmap, submap, cnt_rule_pic
    
    lenk = len(tmpmap)
    左K = -50
    右K = 50
    flag重要级别 = 0    
    cnt_rule_pic = 0
    pos = 0
    for (d, x) in tmpmap.items():
        if '分析结果' in x[1]:
            #日期 = x[0]
            flag, cnt = rules_group_find(tmpmap, d)      #规则组合设计
            if flag >= 1:
                left = -pos
                if left < 左K:
                    left = 左K
                right = lenk-pos
                if right > 右K:
                    right = 右K
                #print(left)
                #print(right)
                for j in range(left, right):
                    submap[tmpmap[d+j][0]] = tmpmap[d+j][1] #submap_index为data
                #endof 'for'
                
                sub_view(submap, code)
               
                submap.clear()
                
                if flag > flag重要级别:
                    flag重要级别 = flag
            #endof 'if'    
        #endof 'if'
        pos = pos + 1
    #end of "for"
        
    if flag重要级别 >= 1:
        #保存当日选股数，最后存入acc
        gl.当天选股数 = gl.当天选股数 + 1

        #选股列表，用于发送email
        if flag重要级别 == 8:
            gl.信息dict['大形态重要'].append(code)
        elif flag重要级别 == 7:
            gl.信息dict['大形态一般'].append(code)
        elif flag重要级别 == 6:
            gl.信息dict['基本形态重要'].append(code)
        elif flag重要级别 == 5:
            gl.信息dict['基本形态一般'].append(code)
        elif flag重要级别 == 1:
            gl.信息dict['形态3个一般'].append(code)
        
        #'a':文件追加写入
        if code[0:1] == '6':
            flag = '\x07\x11'
        elif code[0:1] == '0' or code[0:1] == '3':
            flag = '\x07\x21'
        else:
            flag = '\x07\x24'
        with open(gl.path_view_rst + '导入code_' + getdate() + ".sel", 'a') as out:
            out.write(flag + code)
    #endof "with"
#enf of "def"


#mdl
def mdl_grpview(viewfileoutmap):
    global tmpmap
    
    code = gl.STCode
    i=0
    for (d, x) in viewfileoutmap.items():
        tmpmap[i] = [d, x]
        i = i + 1
    #end of "for"
    #显示满足规则的子图
    sub_grpview_mng(code)
    tmpmap.clear()
    #按照最佳组合、或者一天同时出现多种入了满足时，星号标记
    ##############################mdl_view_ring()
    print("6:grp画图完毕！")
#endof 'def'


