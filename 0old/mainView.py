# -*- coding: gbk -*-
import gl
from subView import mdl_subview
from grpView import mdl_grpview

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections  
#from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
linewidth = 0.2

path_data_avg = "均值整理数据\\"
path_rule_rst = "规则分析结果\\"
path_view_rst = "图片结果\\"

#code

viewfileoutmap = collections.OrderedDict()

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
    global viewfileoutmap, linewidth

    #读取rule分析结果
    #以日期为key，存入map
    with open(gl.path_rule_rst + rule_rst_file, 'r') as f:
        f.readline()
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
    global viewfileoutmap
    
    viewfileoutmap.clear()

    if not os.path.exists(gl.path_data_avg + code + "_avg.txt"):
        return -1
    #读取基本K线数据
    #key为日期
    with open(gl.path_data_avg + code + "_avg.txt", 'r') as f:
        f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # 用tab分割字符串，并保存到列表
            viewfileoutmap[strlist[0]] = {'基K':[float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4])], \
                                          'V':[float(strlist[5]), float(strlist[6]), float(strlist[7])], \
                                          '均':[float(strlist[8]), float(strlist[9]), float(strlist[10]), \
                                          float(strlist[11]), float(strlist[12])]}
        #end of "for"
    #end of "with"

    ##打开rule分析结果文件，数据按key并入viewfileoutmap
    ##研究标的的日期为key
    #read_rule_n_rst(code)
    #read_rule2rst(code)
    #获取code_rule*.txt，并遍历
    files = os.listdir(gl.path_rule_rst)
    for file in files:
        if (code + "_rule") in file:
            read_rule_n_rst(file)  
    #end of "for"
            
    #print(viewfileoutmap)
    return 1
#end of "def"    

def main_view(code):
    global 日期list,总手list,金额list,换手list,\
            均5list,均10list,均20list,均30list,均60list, linewidth
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
        日期list.append(d)
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

    #####fig, ax = plt.subplots()   
    gl.Fig_Cnt = gl.Fig_Cnt 
    fig = plt.figure(gl.Fig_Cnt)                      # Create a `figure' instance
    ax = fig.add_subplot(111) 
    # 设置图的底边距
    fig.subplots_adjust(bottom = 0.25)
   
    
    #plt.grid() #开启网格
    ax.set_xticks(xpos)
    ax.set_xticklabels(日期list, rotation=90, fontsize=10)
    ax.plot(xoffset, 均5list,  '-', alpha = 0.2, color ='y',linewidth=linewidth)
    ax.plot(xoffset, 均10list, '-', alpha = 0.2, color ='yellowgreen',linewidth=linewidth)
    ax.plot(xoffset, 均20list, '-', alpha = 0.2, color ='lightskyblue',linewidth=linewidth)
    ax.plot(xoffset, 均30list, '-', alpha = 0.2, color ='c',linewidth=linewidth)
    ax.plot(xoffset, 均60list, '-', alpha = 0.2, color ='m',linewidth=linewidth)
    
    i = 0
    for (d, x) in viewfileoutmap.items():
        #日期 = d
        开 = x['基K'][0]
        最高 = x['基K'][1]
        最低 = x['基K'][2]
        收 = x['基K'][3]
        
        if 收 > 开:
            ax.bar(xpos[i], 收-开, bottom = 开, width = .4, alpha = .5, facecolor ='r', edgecolor='r',linewidth=linewidth)
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .5, facecolor ='r', edgecolor='r',linewidth=linewidth)
        elif 开 > 收:
            ax.bar(xpos[i], 开-收, bottom = 收, width = .4, alpha = .3, facecolor ='green', edgecolor='green',linewidth=linewidth)
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .3, facecolor ='green', edgecolor='green',linewidth=linewidth)
        else: #开==收:
            ax.bar(xpos[i], 0.005, bottom = 开, width = .4, alpha = .5, facecolor ='r', edgecolor='r',linewidth=linewidth)
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .5, facecolor ='r', edgecolor='r',linewidth=linewidth) 
        #end of "if"
        
        if  '分析结果' in x:
            结果cnt = 0
            for (d2, x2) in x['分析结果'].items():
                #print(日期, d2, x2)
                #画矩形
                squal_x = [xpos[i], xpos[i], xpos[i] + xstep*10, xpos[i] + xstep*10, xpos[i]]
                squal_y = [开, 开*1.2, 开*1.2, 开, 开]
                ax.plot(squal_x, squal_y, '-', alpha = 0.3, color = 'r',linewidth=linewidth)
                #写文字
                ax.text(xpos[i], 开*1.195+结果cnt*0.1, d2+' '+x2, alpha = 0.7, color = 'r', fontsize = 10)
                #ruleID
                ruleID = d2[4:5]
                ax.text(xpos[i], 开*1.187-结果cnt*0.1, '('+ruleID+')', color = 'g', fontsize = 10)
                结果cnt = 结果cnt + 1
            #end of "for"
        #endof "if" 
        
        i = i + 1
    #endof ''for
    if not os.path.exists(path_view_rst+code):    #判断目标是否存在
        os.mkdir(path_view_rst+code)
    fig.savefig(path_view_rst+code+'\\' +code+'.png',  dpi = 600)
    
    fig.clear()
    ax.clear()
    del fig
    del ax
    #plt.show()
#endof "def"        


#mdl
def mdl_mainview():
    code = gl.STCode
    flag = mdl_datafill(code)
    if flag == 1:
        #main_view(code)
        #print("4:mainview画图完毕！")
        
        ##子图
        #mdl_subview(viewfileoutmap)
        
        ##组合图
        mdl_grpview(viewfileoutmap)
    else:
        print("无画图数据！")
    #endof 'if'
#endof 'def'


