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


path_data_avg = "��ֵ��������\\"
path_rule_rst = "����������\\"
path_view_rst = "ͼƬ���\\"

def gettime():
    return time.strftime("%Y%m%d_%H:%M",time.localtime(time.time()))
def getdate(): 
    return time.strftime('%Y%m%d',time.localtime(time.time()))
    
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

���list=[]
���list=[]
        
cnt_rule_pic = 0
xstep = 0.5
offset = (xstep - 0.1) / 2
��trans = 20

def sub_view(submap, code):
    global ����list,����list,���list,����list,\
            ��5list,��10list,��20list,��30list,��60list
    global cnt_rule_pic
     
    ����list.clear()
    ����list.clear()
    ���list.clear()
    ����list.clear()
    ��5list .clear()
    ��10list.clear()
    ��20list.clear()
    ��30list.clear()
    ��60list.clear()
    
    ���list.clear()
    ���list.clear()
    
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
        
        ���list.append(x['��K'][1])
        ���list.append(x['��K'][2])
    #end of "for"
        
    xpos = np.arange(0, len(����list)*xstep, xstep)
    xoffset= xpos + offset
    
    #####fig, ax = plt.subplots()   
    fig = plt.figure(3)                      # Create a `figure' instance
    ax = fig.add_subplot(111)  
    #ax2 = fig.add_subplot(311) 
    #ax3 = fig.add_subplot(312) 
    # ����ͼ�ĵױ߾�
    fig.subplots_adjust(bottom = 0.15)
    fig.subplots_adjust(top = 0.8)
    #fig.subplots_adjust(right = 10)
    #fig.subplots_adjust(left = 0.05)
    #fig.grid() #��������
    ax.set_xticks(xpos)
    ax.set_xticklabels(����list, rotation=90, fontsize=6)
    ax.plot(xoffset, ��5list,  '.-', alpha = 0.5, color ='y')
    ax.plot(xoffset, ��10list, '-', alpha = 0.5, color ='yellowgreen')
    ax.plot(xoffset, ��20list, '-', alpha = 0.5, color ='lightskyblue')
    ax.plot(xoffset, ��30list, '-', alpha = 0.5, color ='c')
    ax.plot(xoffset, ��60list, '-', alpha = 0.5, color ='m')
    
    i = 0
    for (d, x) in submap.items():
        ���� = d
        ���� = x['��K'][0]
        ��� = x['��K'][1]
        ��� = x['��K'][2]
        ���� = x['��K'][3]
        �� = x['��'] 
        �� = x['V']
        V_ma5 = x['V_ma'][0]
        V_ma10= x['V_ma'][1]
        V_ma20 = x['V_ma'][2]
        
        if ���� > ����:
            ax.bar(xpos[i], ����-����, bottom = ����, width = .4, alpha = .5, facecolor ='r', edgecolor='r',linewidth=0.5)
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='r', edgecolor='r',linewidth=0.5)
        elif ���� > ����:
            ax.bar(xpos[i], ����-����, bottom = ����, width = .4, alpha = .5, facecolor ='green', edgecolor='green',linewidth=0.5)
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='green', edgecolor='green',linewidth=0.5)
        else: #����==����:
            ax.bar(xpos[i], 0.005, bottom = ����, width = .4, alpha = .5, facecolor ='r', edgecolor='r',linewidth=0.5)
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='r', edgecolor='r',linewidth=0.5) 
        #end of "if"

        ��btm = min(���list) * 0.9
        ax.bar(xpos[i], 20/��trans, bottom = ��btm, width = .4, alpha = .02, facecolor ='black', edgecolor='black',linewidth=0.5)
        ax.bar(xpos[i], 10/��trans, bottom = ��btm, width = .4, alpha = .025, facecolor ='black', edgecolor='black',linewidth=0.5)
        ax.bar(xpos[i], 5/��trans, bottom = ��btm, width = .4, alpha = .03, facecolor ='black', edgecolor='black',linewidth=0.5)
        ax.bar(xpos[i], 2/��trans, bottom = ��btm, width = .4, alpha = .04, facecolor ='black', edgecolor='black',linewidth=0.5)
        
        �� = �� / ��trans
        if ���� > ����:
            ax.bar(xpos[i], ��, bottom = ��btm, width = .4, alpha = .3, facecolor ='r', edgecolor='r',linewidth=0.5)
        else:
            ax.bar(xpos[i], ��, bottom = ��btm, width = .4, alpha = .3, facecolor ='green', edgecolor='green',linewidth=0.5)
        
            

        if  '�������' in x:
            ���cnt = 0
            #������
            #squal_x = [xpos[i], xpos[i], xpos[i] + xstep*10]
            #squal_y = [����, ����*1.2, ����*1.2]
            squal_x = [xpos[i], xpos[i]]
            squal_y = [����, ����*1.2]
            ax.plot(squal_x, squal_y, '--', alpha = 0.7, color = 'm', linewidth=0.2)
            for (d2, x2) in x['�������'].items():
                #print(����, d2, x2)
                ruleID = d2[4:]
                if not ruleID=='0':
                    #д����
                    ax.text(xpos[i], ����*1.193+���cnt*0.015*����, d2+' '+x2, alpha = 0.7, color = 'r', fontsize = 6)
                    #ruleID
                    ax.text(xpos[i], ����*1.187-���cnt*0.015*����, '('+ruleID+')', color = 'g', fontsize = 6)
                    ���cnt = ���cnt + 1
                #endof 'if'
            #end of "for"
        #end of "if"       
        i = i + 1
    #endof 'for'
            
    if os.path.exists(path_view_rst+code) <= 0:    #�ж�Ŀ���Ƿ����
        os.mkdir(path_view_rst+code)
    cnt_rule_pic = cnt_rule_pic + 1
    fig.savefig(path_view_rst+code+'\\' +code+'_�澯_%d_'%cnt_rule_pic+����+'.png', dpi = 200)

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
    cnt = len(tmpmap[d][1]['�������'])
    if cnt>=2:
        flag = 1
    
    ####����
    if  'rule5' in tmpmap[d][1]['�������']:
        flag = 1 
    if  'rule9' in tmpmap[d][1]['�������']:
        flag = 1 
    if  'rule12' in tmpmap[d][1]['�������']:
        flag = 1 
    if  'rule13' in tmpmap[d][1]['�������']:
        flag = 1 
    if  'rule14' in tmpmap[d][1]['�������']:
        flag = 1 
    if  'rule15' in tmpmap[d][1]['�������']:
        flag = 1     
    if  'rule16' in tmpmap[d][1]['�������']:
        flag = 1 
    if  'rule17' in tmpmap[d][1]['�������']:
        flag = 1 
    if  'rule18' in tmpmap[d][1]['�������']:
        flag = 1 

    ####ר�ò��ԣ����м���        
    if  'rule50' in tmpmap[d][1]['�������']:
        flag = 1    
    if  'rule51' in tmpmap[d][1]['�������']:
        flag = 1   
    if  'rule52' in tmpmap[d][1]['�������']:
        flag = 1   
    if  'rule53' in tmpmap[d][1]['�������']:
        flag = 1   
    if  'rule54' in tmpmap[d][1]['�������']:
        flag = 1   
        
    ####���        
    if  'rule80' in tmpmap[d][1]['�������']:
        flag = 1    
    if  'rule81' in tmpmap[d][1]['�������']:
        flag = 1   
    if  'rule82' in tmpmap[d][1]['�������']:
        flag = 1   
    
    return flag, cnt    
#endof 'def'


def sub_grpview_mng(code):
    global tmpmap, submap, cnt_rule_pic
    
    lenk = len(tmpmap)
    ��K = -50
    ��K = 50
    mark = 0    
    cnt_rule_pic = 0
    pos = 0
    for (d, x) in tmpmap.items():
        if '�������' in x[1]:
            #���� = x[0]
            flag, cnt = rules_group_find(tmpmap, d)      #����������
            if flag == 1:
                left = -pos
                if left < ��K:
                    left = ��K
                right = lenk-pos
                if right > ��K:
                    right = ��K
                #print(left)
                #print(right)
                for j in range(left, right):
                    submap[tmpmap[d+j][0]] = tmpmap[d+j][1] #submap_indexΪdata
                #endof 'for'
                
                sub_view(submap, code)
               
                submap.clear()
                mark = 1
            #endof 'if'    
        #endof 'if'
        pos = pos + 1
    #end of "for"
    if mark == 1:
        #'a':�ļ�׷��д��
        if code[0:1] == '6':
            flag = '\x07\x11'
        elif code[0:1] == '0' or code[0:1] == '3':
            flag = '\x07\x21'
        else:
            flag = '\x07\x24'
        with open(gl.path_view_rst + '����code_' + getdate() + ".sel", 'a') as out:
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
    #��ʾ����������ͼ
    sub_grpview_mng(code)
    tmpmap.clear()
    #���������ϡ�����һ��ͬʱ���ֶ�����������ʱ���Ǻű��
    ##############################mdl_view_ring()
    print("6:grp��ͼ��ϣ�")
#endof 'def'


