# -*- coding: gbk -*-
import gl
from ruleLib.rule1 import rule_1
from ruleLib.rule2 import rule_2

#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib as mpl
import collections
import os

Outmap = collections.OrderedDict()  
Anlyinmap = collections.OrderedDict()  
rules = []

'''��ȡ����K������'''
def mdl_read(code):
    global Outmap, Anlyinmap
    
    Outmap.clear()
    Anlyinmap.clear()

    if os.path.exists(gl.path_data_avg + code + "_avg.txt") <= 0:
        return -1
    ##��K���ļ������ݰ�key����Outmap
    ##�о���ĵ�����Ϊkey
    with open(gl.path_data_avg + code + "_avg.txt", 'r') as f:
        f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # ��tab�ָ��ַ����������浽�б�
            Outmap[strlist[0]] = {'��K':[float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4])], \
                                  'V':[float(strlist[5]), float(strlist[6]), float(strlist[7])], \
                                  '��':[float(strlist[8]), float(strlist[9]), float(strlist[10]), \
                                        float(strlist[11]), float(strlist[12])]}
        #end of "for"
    #end of "with"

    '''��ȡ���������������ݣ������K����Ϣ�棩��������key����outmap'''

    '''outmap��key����i++���'''
    i = 0
    for (d,x) in Outmap.items():
        Anlyinmap[i] = x
        Anlyinmap[i]['date'] = d
        i = i + 1
    #end of "for"
#end of "def"


'''��ȡrules'''
def mdl_ruleget(code):
    global rules
    
    #������Ϊ���� �ַ��������Ӧ�ĺ���������
    
    if 1==1:
        rules.append({'һ��������', 'rule1'})
    if 1==2:
        rules.append({'�Ϳ�����', 'rule2'})
#end of "def"


'''�������ݷ���'''
def mdl_ruleanlys(code):
    rule_1(code, Anlyinmap)
    rule_2(code, Anlyinmap)
#end of "def"


#��ȡ*.txt��������
def mdl_ruleAnalyse():
    code = gl.STCode
    mdl_read(code)
    mdl_ruleget(code)
    mdl_ruleanlys(code)
    print(code)
    print("3:rules������ϣ�")
#endof 'mdl'


