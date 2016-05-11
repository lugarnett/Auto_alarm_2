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


path_data_avg = "��ֵ��������\\"
path_rule_rst = "����������\\"
path_view_rst = "ͼƬ���\\"

#code

viewfileoutmap = collections.OrderedDict()
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

def read_rule_n_rst(rule_rst_file):

    #��ȡrule�������
    #������Ϊkey������map
    with open(path_rule_rst + rule_rst_file, 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # ��tab�ָ��ַ����������浽�б�
            if(strlist[0] in viewfileoutmap):   #���ڴ���
                if '�������' in viewfileoutmap[strlist[0]]:    #�Ѿ����ڽ�����ݣ���ô��Ҫ����
                    viewfileoutmap[strlist[0]]['�������'][strlist[1]] = strlist[2]
                else:
                    viewfileoutmap[strlist[0]]['�������'] = {strlist[1]: strlist[2]}
        #end of "for"
    #end of "with"
#end of "def"


xstep = 0.5
offset = (xstep - 0.1) / 2
    
def mdl_datafill(code):

    viewfileoutmap.clear()
    day = 0

    #��ȡ����K������
    #keyΪ����
    with open(path_data_avg + code + "_avg.txt", 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # ��tab�ָ��ַ����������浽�б�
            viewfileoutmap[strlist[0]] = {'��K':[float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4])], \
                                          'V':[int(strlist[5]), int(strlist[6]), float(strlist[7])], \
                                          '��':[float(strlist[8]), float(strlist[9]), float(strlist[10]), float(strlist[11]), \
                                               float(strlist[12])]}
            day = day + 1
        #end of "for"
    #end of "with"

    ##��rule��������ļ������ݰ�key����viewfileoutmap
    ##�о���ĵ�����Ϊkey
    #read_rule_n_rst(code)
    #read_rule2rst(code)
    #��ȡcode_rule*.txt��������
    files = os.listdir(path_rule_rst)
    for file in files:
        if (code + "_rule") in file:
            read_rule_n_rst(file)  
    #end of "for"
#end of "def"    

def mdl_view():
    ����list.clear()
    ����list.clear()
    ���list.clear()
    ����list.clear()
    ��5list .clear()
    ��10list.clear()
    ��20list.clear()
    ��30list.clear()
    ��60list.clear()
    for (d,x) in viewfileoutmap.items():
        if d.find("һ") > 0:
            ����list.append(d[:8])
        else:
            ����list.append("")
        #����Klist.append(x["��K"])
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
    
    fig, ax = plt.subplots()   
    # ����ͼ�ĵױ߾�
    plt.subplots_adjust(bottom = 0.15)
    #plt.subplots_adjust(right = 0.5)
    #plt.subplots_adjust(left = 0.05)
    #plt.subplots_adjust(top = 10)
    #plt.grid() #��������
    ax.set_xticks(xpos)
    ax.set_xticklabels(����list, rotation=90, fontsize=10)
    plt.plot(xoffset, ��5list,  '-', alpha = 0.2, color ='y')
    plt.plot(xoffset, ��10list, '-', alpha = 0.2, color ='yellowgreen')
    plt.plot(xoffset, ��20list, '-', alpha = 0.2, color ='lightskyblue')
    plt.plot(xoffset, ��30list, '-', alpha = 0.2, color ='c')
    plt.plot(xoffset, ��60list, '-', alpha = 0.2, color ='m')
    
    i = 0
    for (d, x) in viewfileoutmap.items():
        ���� = d
        ���� = x['��K'][0]
        ��� = x['��K'][1]
        ��� = x['��K'][2]
        ���� = x['��K'][3]
        
        if ���� > ����:
            ax.bar(xpos[i], ����-����, bottom = ����, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='r', edgecolor='r')
        elif ���� > ����:
            ax.bar(xpos[i], ����-����, bottom = ����, width = .4, alpha = .3, facecolor ='green', edgecolor='green')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .3, facecolor ='green', edgecolor='green')
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
                ruleID = x2[4:5]
                plt.plot(squal_x, squal_y, '-', alpha = 0.3, color = 'r')
                #д����
                ax.text(xpos[i], ����*1.2, d2+' '+x2, alpha = 0.3, color = 'r', fontsize = 5)
                #ruleID
                ax.text(xpos[i]+(int(ruleID)-1)*0.7, ����*1.15, '('+ruleID+')', color = 'g', fontsize = 8)
            #end of "for"
        #end of "if"       
        i = i + 1
#end of "def"        


def mdl_sub_view(submap):
     
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
        if d.find("һ") > 0:
            ����list.append(d[:8])
        else:
            ����list.append("")
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
    plt.subplots_adjust(bottom = 0.15)
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
                ruleID = x2[4:5]
                plt.plot(squal_x, squal_y, '-', alpha = 0.3, color = 'r')
                #д����
                ax.text(xpos[i], ����*1.2, d2+' '+x2, alpha = 0.3, color = 'r', fontsize = 8)
                #ruleID
                ax.text(xpos[i]+(int(ruleID)-1)*0.7, ����*1.15, '('+ruleID+')', color = 'g', fontsize = 8)
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
        if  '�������' in x[1]:
            for j in range(-20,50):
                submap[tmpmap[d+j][0]] = tmpmap[d+j][1]
            
            mdl_sub_view(submap)
            cnt_rule_pic = cnt_rule_pic + 1
            plt.savefig(path_view_rst + code + '_' + '%d'%cnt_rule_pic + '.png')
            #plt.show()
            submap.clear()
    #end of "for"   

#enf of "def"
    
#���ص�ǰʱ��
def gettime():
    return time.strftime("%Y%2m2%d_%H:%M",time.localtime(time.time()))

#main()
#��ȡ*_avg.txt��������
files = os.listdir(path_data_avg)
for file in files:
    if "_avg.txt" in file or "_avg.TXT" in file:
        if len(file) == 14:
            code = file[:6]
            mdl_datafill(code)
            mdl_view()
            plt.savefig(path_view_rst + code + '.png',  dpi = 600)
            #plt.show()
            #��ʾ����������ͼ
            mdl_sub_view_mng(code)
            #���������ϡ�����һ��ͬʱ���ֶ�����������ʱ���Ǻű��
            ##############################mdl_view_ring()
#end of "for"
print("��ͼ��ϣ�\n")



