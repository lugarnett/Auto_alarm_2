# -*- coding: gbk -*-
import gl

import time
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections  
#from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


path_data_avg = "均值整理数据\\"
path_rule_rst = "规则分析结果\\"
path_view_rst = "图片结果\\"

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
        ax.bar(xpos[i], 2/换trans, bottom = 换btm, width = .4, alpha = .04, facecolor ='black', edgecolor='black',linewidth=0.5)
        
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
            squal_x = [xpos[i], xpos[i]]
            squal_y = [开盘, 开盘*1.2]
            ax.plot(squal_x, squal_y, '--', alpha = 0.7, color = 'm', linewidth=0.2)
            for (d2, x2) in x['分析结果'].items():
                #print(日期, d2, x2)
                ruleID = d2[4:]
                if not ruleID=='0':
                    #写文字
                    ax.text(xpos[i], 开盘*1.193+结果cnt*0.015*开盘, d2+' '+x2, alpha = 0.7, color = 'r', fontsize = 6)
                    #ruleID
                    ax.text(xpos[i], 开盘*1.187-结果cnt*0.015*开盘, '('+ruleID+')', color = 'g', fontsize = 6)
                    结果cnt = 结果cnt + 1
                #endof 'if'
            #end of "for"
        #end of "if"       
        i = i + 1
    #endof 'for'
            
    if os.path.exists(path_view_rst+code) <= 0:    #判断目标是否存在
        os.mkdir(path_view_rst+code)
    cnt_rule_pic = cnt_rule_pic + 1
    fig.savefig(path_view_rst+code+'\\' +code+'_告警_%d_'%cnt_rule_pic+日期+'.png', dpi = 200)

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
    cnt = len(tmpmap[d][1]['分析结果'])
    if cnt>=2:
        flag = 1
    
    ####基本
    if  'rule5' in tmpmap[d][1]['分析结果']:
        flag = 1 
    if  'rule9' in tmpmap[d][1]['分析结果']:
        flag = 1 
    if  'rule12' in tmpmap[d][1]['分析结果']:
        flag = 1 
    if  'rule13' in tmpmap[d][1]['分析结果']:
        flag = 1 
    if  'rule14' in tmpmap[d][1]['分析结果']:
        flag = 1 
    if  'rule15' in tmpmap[d][1]['分析结果']:
        flag = 1     
    if  'rule16' in tmpmap[d][1]['分析结果']:
        flag = 1 
    if  'rule17' in tmpmap[d][1]['分析结果']:
        flag = 1 
    if  'rule18' in tmpmap[d][1]['分析结果']:
        flag = 1 

    ####专用策略：空中加油        
    if  'rule50' in tmpmap[d][1]['分析结果']:
        flag = 1    
    if  'rule51' in tmpmap[d][1]['分析结果']:
        flag = 1   
    if  'rule52' in tmpmap[d][1]['分析结果']:
        flag = 1   
    if  'rule53' in tmpmap[d][1]['分析结果']:
        flag = 1   
    if  'rule54' in tmpmap[d][1]['分析结果']:
        flag = 1   
        
    ####组合        
    if  'rule80' in tmpmap[d][1]['分析结果']:
        flag = 1    
    if  'rule81' in tmpmap[d][1]['分析结果']:
        flag = 1   
    if  'rule82' in tmpmap[d][1]['分析结果']:
        flag = 1   
    
    return flag, cnt    
#endof 'def'


def sub_grpview_mng(code):
    global tmpmap, submap, cnt_rule_pic
    
    lenk = len(tmpmap)
    左K = -50
    右K = 50
    mark = 0    
    cnt_rule_pic = 0
    pos = 0
    for (d, x) in tmpmap.items():
        if '分析结果' in x[1]:
            #日期 = x[0]
            flag, cnt = rules_group_find(tmpmap, d)      #规则组合设计
            if flag == 1:
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
                mark = 1
            #endof 'if'    
        #endof 'if'
        pos = pos + 1
    #end of "for"
    if mark == 1:
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


