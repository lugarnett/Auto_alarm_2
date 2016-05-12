# -*- coding: gbk -*-
import gl

import time
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections  
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


path_data_avg = "均值整理数据\\"
path_rule_rst = "规则分析结果\\"
path_view_rst = "图片结果\\"

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


xstep = 0.5
offset = (xstep - 0.1) / 2

def sub_view(submap):
     
    日期list.clear()
    总手list.clear()
    金额list.clear()
    换手list.clear()
    均5list .clear()
    均10list.clear()
    均20list.clear()
    均30list.clear()
    均60list.clear()
    
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
    #end of "for"
        
    xpos = np.arange(0, len(日期list)*xstep, xstep)
    xoffset= xpos + offset
    
    fig, ax = plt.subplots(figsize = (8, 4))   
    # 设置图的底边距
    plt.subplots_adjust(bottom = 0.25)
    #plt.subplots_adjust(right = 0.5)
    #plt.subplots_adjust(left = 0.05)
    #plt.subplots_adjust(top = 10)
    #plt.grid() #开启网格
    ax.set_xticks(xpos)
    ax.set_xticklabels(日期list, rotation=90, fontsize=10)
    plt.plot(xoffset, 均5list,  '.-', alpha = 0.5, color ='y')
    plt.plot(xoffset, 均10list, '-', alpha = 0.5, color ='yellowgreen')
    plt.plot(xoffset, 均20list, '-', alpha = 0.5, color ='lightskyblue')
    plt.plot(xoffset, 均30list, '-', alpha = 0.5, color ='c')
    plt.plot(xoffset, 均60list, '-', alpha = 0.5, color ='m')
    
    i = 0
    for (d, x) in submap.items():
        日期 = d
        开盘 = x['基K'][0]
        最高 = x['基K'][1]
        最低 = x['基K'][2]
        收盘 = x['基K'][3]
        
        if 收盘 > 开盘:
            ax.bar(xpos[i], 收盘-开盘, bottom = 开盘, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .5, facecolor ='r', edgecolor='r')
        elif 开盘 > 收盘:
            ax.bar(xpos[i], 开盘-收盘, bottom = 收盘, width = .4, alpha = .5, facecolor ='green', edgecolor='green')
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .5, facecolor ='green', edgecolor='green')
        else: #开盘==收盘:
            ax.bar(xpos[i], 0.005, bottom = 开盘, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .5, facecolor ='r', edgecolor='r') 
        #end of "if"

        if  '分析结果' in x:
            for (d2, x2) in x['分析结果'].items():
                #print(日期, d2, x2)
                #画矩形
                squal_x = [xpos[i], xpos[i], xpos[i] + xstep*10, xpos[i] + xstep*10, xpos[i]]
                squal_y = [开盘, 开盘*1.2, 开盘*1.2, 开盘, 开盘]
                ruleID = d2[4:5]
                plt.plot(squal_x, squal_y, '-', alpha = 0.3, color = 'r')
                #写文字
                ax.text(xpos[i], 开盘*1.2, d2+' '+x2, alpha = 0.3, color = 'r', fontsize = 8)
                #ruleID
                ax.text(xpos[i]+(int(ruleID)-1)*0.7, 开盘*1.15, '('+ruleID+')', color = 'g', fontsize = 8)
            #end of "for"
        #end of "if"       
        i = i + 1
#end of "def"

def sub_view_mng(viewfileoutmap, code):
    i=0
    for (d, x) in viewfileoutmap.items():
        tmpmap[i] = [d, x]
        i = i + 1
    #end of "for"
    
    lenk = i
    left = -20
    right = 50
        
    cnt_rule_pic = 0
    pos = 0
    for (d, x) in tmpmap.items():
        if  '分析结果' in x[1]:
            left = -pos
            if left < -20:
                left = -20
            right = lenk-pos
            if right > 50:
                right = 50
            #print(left)
            #print(right)
            for j in range(left, right):
                submap[tmpmap[d+j][0]] = tmpmap[d+j][1]
            
            sub_view(submap)
    
            if os.path.exists(path_view_rst+code) <= 0:    #判断目标是否存在
                os.mkdir(path_view_rst+code)
            cnt_rule_pic = cnt_rule_pic + 1
            plt.savefig(path_view_rst+code+'\\' +code+'_%d'%cnt_rule_pic+'.png', dpi = 100)
            #plt.show()
            submap.clear()
        #endof 'if'
        pos = pos + 1
    #end of "for"   

#enf of "def"
    
#返回当前时间
def gettime():
    return time.strftime("%Y%2m2%d_%H:%M",time.localtime(time.time()))


#mdl
def mdl_subview(viewfileoutmap):
    
    code = gl.STCode
    #显示满足规则的子图
    sub_view_mng(viewfileoutmap, code)
    #按照最佳组合、或者一天同时出现多种入了满足时，星号标记
    ##############################mdl_view_ring()
    print("5:sub画图完毕！")
#endof 'def'


