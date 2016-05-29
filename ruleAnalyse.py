# -*- coding: gbk -*-
import gl
from ruleLib.rule1 import rule_1
from ruleLib.rule2 import rule_2
from ruleLib.rule3 import rule_3
from ruleLib.rule4 import rule_4
from ruleLib.rule5 import rule_5
from ruleLib.rule6 import rule_6
from ruleLib.rule7 import rule_7
from ruleLib.rule8 import rule_8
from ruleLib.rule9 import rule_9
from ruleLib.rule10 import rule_10
from ruleLib.rule80 import rule_80
from ruleLib.rule81 import rule_81

#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib as mpl
import collections
import os

Outmap = collections.OrderedDict()  
Anlyinmap = collections.OrderedDict()  
rules = []

'''读取基本K线数据'''
def mdl_read(code):
    global Outmap, Anlyinmap
    
    Outmap.clear()
    Anlyinmap.clear()

    if os.path.exists(gl.path_data_avg + code + "_avg.txt") <= 0:
        return -1
    ##打开K线文件，数据按key并入Outmap
    ##研究标的的日期为key
    with open(gl.path_data_avg + code + "_avg.txt", 'r') as f:
        f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # 用tab分割字符串，并保存到列表
            Outmap[strlist[0]] = {'基K':[float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4])], \
                                  'V':[float(strlist[5]), float(strlist[6]), float(strlist[7])], \
                                  '均':[float(strlist[8]), float(strlist[9]), float(strlist[10]), \
                                        float(strlist[11]), float(strlist[12])]}
        #end of "for"
    #end of "with"

    '''读取其他分析输入数据（如大盘K、消息面），按日期key并入outmap'''

    '''outmap的key换成i++序号'''
    i = 0
    for (d,x) in Outmap.items():
        Anlyinmap[i] = x
        Anlyinmap[i]['date'] = d
        i = i + 1
    #end of "for"
    return 1
#end of "def"


'''读取rules'''
def mdl_ruleget(code):
    global rules
    
    #初步定为采用 字符串数组对应的函数名数组
    
    if 1==1:
        rules.append({'一阳穿五线', 'rule1'})
    if 1==2:
        rules.append({'低开长阳', 'rule2'})
#end of "def"


'''进行数据分析'''
def mdl_ruleanlys(code):
    '''rule_1(code, Anlyinmap)
    rule_2(code, Anlyinmap)
    rule_3(code, Anlyinmap)
    rule_4(code, Anlyinmap)
    rule_5(code, Anlyinmap)
    rule_6(code, Anlyinmap)
    rule_7(code, Anlyinmap)
    rule_8(code, Anlyinmap)
    rule_9(code, Anlyinmap)
    rule_10(code, Anlyinmap)
    rule_80(code, Anlyinmap)'''
    rule_81(code, Anlyinmap)
#end of "def"


#获取*.txt，并遍历
def mdl_ruleAnalyse():
    code = gl.STCode
    flag = mdl_read(code)
    if flag == 1:
        mdl_ruleget(code)
        mdl_ruleanlys(code)
        print("3:rules分析完毕！")
    else:
        print("3:rules分析无数据。。。")

#endof 'mdl'


