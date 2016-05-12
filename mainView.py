# -*- coding: gbk -*-
import gl
from subView import mdl_subview
from grpView import mdl_grpview

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
    with open(gl.path_rule_rst + rule_rst_file, 'r') as f:
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

    if not os.path.exists(gl.path_data_avg + code + "_avg.txt"):
        return -1
    #��ȡ����K������
    #keyΪ����
    with open(gl.path_data_avg + code + "_avg.txt", 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # ��tab�ָ��ַ����������浽�б�
            viewfileoutmap[strlist[0]] = {'��K':[float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4])], \
                                          'V':[float(strlist[5]), float(strlist[6]), float(strlist[7])], \
                                          '��':[float(strlist[8]), float(strlist[9]), float(strlist[10]), \
                                          float(strlist[11]), float(strlist[12])]}
            day = day + 1
        #end of "for"
    #end of "with"

    ##��rule��������ļ������ݰ�key����viewfileoutmap
    ##�о���ĵ�����Ϊkey
    #read_rule_n_rst(code)
    #read_rule2rst(code)
    #��ȡcode_rule*.txt��������
    files = os.listdir(gl.path_rule_rst)
    for file in files:
        if (code + "_rule") in file:
            read_rule_n_rst(file)  
    #end of "for"
            
    #print(viewfileoutmap)
    return 1
#end of "def"    

def main_view():
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
        ����list.append(d)
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
    plt.subplots_adjust(bottom = 0.25)
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
        �� = x['��K'][0]
        ��� = x['��K'][1]
        ��� = x['��K'][2]
        �� = x['��K'][3]
        
        if �� > ��:
            ax.bar(xpos[i], ��-��, bottom = ��, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='r', edgecolor='r')
        elif �� > ��:
            ax.bar(xpos[i], ��-��, bottom = ��, width = .4, alpha = .3, facecolor ='green', edgecolor='green')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .3, facecolor ='green', edgecolor='green')
        else: #��==��:
            ax.bar(xpos[i], 0.005, bottom = ��, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='r', edgecolor='r') 
        #end of "if"
        
        if  '�������' in x:
            for (d2, x2) in x['�������'].items():
                #print(����, d2, x2)
                #������
                squal_x = [xpos[i], xpos[i], xpos[i] + xstep*10, xpos[i] + xstep*10, xpos[i]]
                squal_y = [��, ��*1.2, ��*1.2, ��, ��]
                plt.plot(squal_x, squal_y, '-', alpha = 0.3, color = 'r')
                #д����
                ax.text(xpos[i], ��*1.2, d2+' '+x2, alpha = 0.3, color = 'r', fontsize = 5)
                #ruleID
                ruleID = d2[4:5]
                ax.text(xpos[i]+(float(ruleID)-1)*0.7, ��*1.15, '('+ruleID+')', color = 'g', fontsize = 8)
            #end of "for"
        #end of "if" 
        
        i = i + 1
#end of "def"        


#mdl
def mdl_mainview():
    code = gl.STCode
    flag = mdl_datafill(code)
    if flag == 1:
        main_view()
        
        if not os.path.exists(path_view_rst+code):    #�ж�Ŀ���Ƿ����
            os.mkdir(path_view_rst+code)
        plt.savefig(path_view_rst+code+'\\' +code+'.png',  dpi = 600)
        #plt.show()
        print("4:mainview��ͼ��ϣ�")
        
        ##��ͼ
        #mdl_subview(viewfileoutmap)
        
        ##���ͼ
        mdl_grpview(viewfileoutmap)
    else:
        print("�޻�ͼ���ݣ�")
    #endof 'if'
#endof 'def'


