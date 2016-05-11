# -*- coding: gbk -*-
'''
'%d'%int(height)

'''

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

#code

viewfileoutmap = collections.OrderedDict()
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

def read_rule_n_rst(rule_rst_file):

    #读取rule分析结果
    #以日期为key，存入map
    with open(path_rule_rst + rule_rst_file, 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # 用tab分割字符串，并保存到列表
            if(strlist[0] in viewfileoutmap):   #日期存在
                if '分析结果' in viewfileoutmap[strlist[0]]:    #已经存在结果数据，那么需要新增
                    viewfileoutmap[strlist[0]]['分析结果'][strlist[1]] = strlist[2]
                else:
                    viewfileoutmap[strlist[0]]['分析结果'] = {strlist[1]: strlist[2]}
        #end of "for"
    #end of "with"
#end of "def"


xstep = 0.5
offset = (xstep - 0.1) / 2
    
def mdl_datafill(code):

    viewfileoutmap.clear()
    day = 0

    #读取基本K线数据
    #key为日期
    with open(path_data_avg + code + "_avg.txt", 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # 用tab分割字符串，并保存到列表
            viewfileoutmap[strlist[0]] = {'基K':[float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4])], \
                                          'V':[int(strlist[5]), int(strlist[6]), float(strlist[7])], \
                                          '均':[float(strlist[8]), float(strlist[9]), float(strlist[10]), float(strlist[11]), \
                                               float(strlist[12])]}
            day = day + 1
        #end of "for"
    #end of "with"

    ##打开rule分析结果文件，数据按key并入viewfileoutmap
    ##研究标的的日期为key
    #read_rule_n_rst(code)
    #read_rule2rst(code)
    #获取code_rule*.txt，并遍历
    files = os.listdir(path_rule_rst)
    for file in files:
        if (code + "_rule") in file:
            read_rule_n_rst(file)  
    #end of "for"
#end of "def"    

def mdl_view():
    日期list.clear()
    总手list.clear()
    金额list.clear()
    换手list.clear()
    均5list .clear()
    均10list.clear()
    均20list.clear()
    均30list.clear()
    均60list.clear()
    for (d,x) in viewfileoutmap.items():
        if d.find("一") > 0:
            日期list.append(d[:8])
        else:
            日期list.append("")
        #个股Klist.append(x["基K"])
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
    
    fig, ax = plt.subplots()   
    # 设置图的底边距
    plt.subplots_adjust(bottom = 0.15)
    #plt.subplots_adjust(right = 0.5)
    #plt.subplots_adjust(left = 0.05)
    #plt.subplots_adjust(top = 10)
    #plt.grid() #开启网格
    ax.set_xticks(xpos)
    ax.set_xticklabels(日期list, rotation=90, fontsize=10)
    plt.plot(xoffset, 均5list,  '-', alpha = 0.2, color ='y')
    plt.plot(xoffset, 均10list, '-', alpha = 0.2, color ='yellowgreen')
    plt.plot(xoffset, 均20list, '-', alpha = 0.2, color ='lightskyblue')
    plt.plot(xoffset, 均30list, '-', alpha = 0.2, color ='c')
    plt.plot(xoffset, 均60list, '-', alpha = 0.2, color ='m')
    
    i = 0
    for (d, x) in viewfileoutmap.items():
        日期 = d
        开盘 = x['基K'][0]
        最高 = x['基K'][1]
        最低 = x['基K'][2]
        收盘 = x['基K'][3]
        
        if 收盘 > 开盘:
            ax.bar(xpos[i], 收盘-开盘, bottom = 开盘, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .5, facecolor ='r', edgecolor='r')
        elif 开盘 > 收盘:
            ax.bar(xpos[i], 开盘-收盘, bottom = 收盘, width = .4, alpha = .3, facecolor ='green', edgecolor='green')
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .3, facecolor ='green', edgecolor='green')
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
                ruleID = x2[4:5]
                plt.plot(squal_x, squal_y, '-', alpha = 0.3, color = 'r')
                #写文字
                ax.text(xpos[i], 开盘*1.2, d2+' '+x2, alpha = 0.3, color = 'r', fontsize = 5)
                #ruleID
                ax.text(xpos[i]+(int(ruleID)-1)*0.7, 开盘*1.15, '('+ruleID+')', color = 'g', fontsize = 8)
            #end of "for"
        #end of "if"       
        i = i + 1
#end of "def"        


def mdl_sub_view(submap):
     
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
        if d.find("一") > 0:
            日期list.append(d[:8])
        else:
            日期list.append("")
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
    plt.subplots_adjust(bottom = 0.15)
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
                ruleID = x2[4:5]
                plt.plot(squal_x, squal_y, '-', alpha = 0.3, color = 'r')
                #写文字
                ax.text(xpos[i], 开盘*1.2, d2+' '+x2, alpha = 0.3, color = 'r', fontsize = 8)
                #ruleID
                ax.text(xpos[i]+(int(ruleID)-1)*0.7, 开盘*1.15, '('+ruleID+')', color = 'g', fontsize = 8)
            #end of "for"
        #end of "if"       
        i = i + 1
#end of "def"

def mdl_sub_view_mng(code):
    i=0
    for (d, x) in viewfileoutmap.items():
        tmpmap[i] = [d, x]
        i = i + 1
    #end of "for"

    cnt_rule_pic = 0
    for (d, x) in tmpmap.items():
        if  '分析结果' in x[1]:
            for j in range(-20,50):
                submap[tmpmap[d+j][0]] = tmpmap[d+j][1]
            
            mdl_sub_view(submap)
            cnt_rule_pic = cnt_rule_pic + 1
            plt.savefig(path_view_rst + code + '_' + '%d'%cnt_rule_pic + '.png')
            #plt.show()
            submap.clear()
    #end of "for"   

#enf of "def"
    
#返回当前时间
def gettime():
    return time.strftime("%Y%2m2%d_%H:%M",time.localtime(time.time()))

#main()
#获取*_avg.txt，并遍历
files = os.listdir(path_data_avg)
for file in files:
    if "_avg.txt" in file or "_avg.TXT" in file:
        if len(file) == 14:
            code = file[:6]
            mdl_datafill(code)
            mdl_view()
            plt.savefig(path_view_rst + code + '.png',  dpi = 600)
            #plt.show()
            #显示满足规则的子图
            mdl_sub_view_mng(code)
            #按照最佳组合、或者一天同时出现多种入了满足时，星号标记
            ##############################mdl_view_ring()
#end of "for"
print("画图完毕！\n")



