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


path_data_avg = "��ֵ��������\\"
path_rule_rst = "����������\\"
path_view_rst = "ͼƬ���\\"

tmpmap = collections.OrderedDict()
submap = collections.OrderedDict()

����list=[]
#����Klist=[]
����list=[]
���list=[]
����list=[]
��5list =[]
��10list=[]
��20list=[]
��30list=[]
��60list=[]


xstep = 0.5
offset = (xstep - 0.1) / 2

def sub_view(submap):
     
    ����list.clear()
    ����list.clear()
    ���list.clear()
    ����list.clear()
    ��5list .clear()
    ��10list.clear()
    ��20list.clear()
    ��30list.clear()
    ��60list.clear()
    
    for (d,x) in submap.items():
        ����list.append(d)
        ����list.append(x["V"][0])
        ���list.append(x["V"][1])
        ����list.append(x["V"][2])
        ��5list.append(x["��"][0])
        ��10list.append(x["��"][1])
        ��20list.append(x["��"][2])
        ��30list.append(x["��"][3])
        ��60list.append(x["��"][4])
    #end of "for"
        
    xpos = np.arange(0, len(����list)*xstep, xstep)
    xoffset= xpos + offset
    
    fig, ax = plt.subplots(figsize = (8, 4))   
    # ����ͼ�ĵױ߾�
    plt.subplots_adjust(bottom = 0.25)
    #plt.subplots_adjust(right = 0.5)
    #plt.subplots_adjust(left = 0.05)
    #plt.subplots_adjust(top = 10)
    #plt.grid() #��������
    ax.set_xticks(xpos)
    ax.set_xticklabels(����list, rotation=90, fontsize=10)
    plt.plot(xoffset, ��5list,  '.-', alpha = 0.5, color ='y')
    plt.plot(xoffset, ��10list, '-', alpha = 0.5, color ='yellowgreen')
    plt.plot(xoffset, ��20list, '-', alpha = 0.5, color ='lightskyblue')
    plt.plot(xoffset, ��30list, '-', alpha = 0.5, color ='c')
    plt.plot(xoffset, ��60list, '-', alpha = 0.5, color ='m')
    
    i = 0
    for (d, x) in submap.items():
        ���� = d
        ���� = x['��K'][0]
        ��� = x['��K'][1]
        ��� = x['��K'][2]
        ���� = x['��K'][3]
        
        if ���� > ����:
            ax.bar(xpos[i], ����-����, bottom = ����, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='r', edgecolor='r')
        elif ���� > ����:
            ax.bar(xpos[i], ����-����, bottom = ����, width = .4, alpha = .5, facecolor ='green', edgecolor='green')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='green', edgecolor='green')
        else: #����==����:
            ax.bar(xpos[i], 0.005, bottom = ����, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='r', edgecolor='r') 
        #end of "if"

        if  '�������' in x:
            for (d2, x2) in x['�������'].items():
                #print(����, d2, x2)
                #������
                squal_x = [xpos[i], xpos[i], xpos[i] + xstep*10, xpos[i] + xstep*10, xpos[i]]
                squal_y = [����, ����*1.2, ����*1.2, ����, ����]
                ruleID = d2[4:5]
                plt.plot(squal_x, squal_y, '-', alpha = 0.3, color = 'r')
                #д����
                ax.text(xpos[i], ����*1.2, d2+' '+x2, alpha = 0.3, color = 'r', fontsize = 8)
                #ruleID
                ax.text(xpos[i]+(int(ruleID)-1)*0.7, ����*1.15, '('+ruleID+')', color = 'g', fontsize = 8)
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
        if  '�������' in x[1]:
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
    
            if os.path.exists(path_view_rst+code) <= 0:    #�ж�Ŀ���Ƿ����
                os.mkdir(path_view_rst+code)
            cnt_rule_pic = cnt_rule_pic + 1
            plt.savefig(path_view_rst+code+'\\' +code+'_%d'%cnt_rule_pic+'.png', dpi = 100)
            #plt.show()
            submap.clear()
        #endof 'if'
        pos = pos + 1
    #end of "for"   

#enf of "def"
    
#���ص�ǰʱ��
def gettime():
    return time.strftime("%Y%2m2%d_%H:%M",time.localtime(time.time()))


#mdl
def mdl_subview(viewfileoutmap):
    
    code = gl.STCode
    #��ʾ����������ͼ
    sub_view_mng(viewfileoutmap, code)
    #���������ϡ�����һ��ͬʱ���ֶ�����������ʱ���Ǻű��
    ##############################mdl_view_ring()
    print("5:sub��ͼ��ϣ�")
#endof 'def'


