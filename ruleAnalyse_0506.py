# -*- coding: gbk -*-

path_rule_rst = '规则分析结果\\'
path_data_avg = '均值整理数据\\'

#code = "002234"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections
import os

Outmap = collections.OrderedDict()  
rules = []

Anlyinmap = collections.OrderedDict()  
Anlyoutmap = collections.OrderedDict()  


'''读取基本K线数据'''
def mdl_read(code):
    Outmap.clear()
    Anlyinmap.clear()

    ##打开K线文件，数据按key并入Outmap
    ##研究标的的日期为key
    with open(path_data_avg + code + "_avg.txt", 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # 用tab分割字符串，并保存到列表
            Outmap[strlist[0]] = {'基K':[float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4])], \
                                  'V':[int(strlist[5]), int(strlist[6]), float(strlist[7])], \
                                  '均':[float(strlist[8]), float(strlist[9]), float(strlist[10]), float(strlist[11]), \
                                       float(strlist[12])]}
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
#end of "def"


'''读取rules'''
def mdl_ruleget(code):
    #初步定为采用 字符串数组对应的函数名数组
    
    if 1==1:
        rules.append({'一阳穿五线', 'rule1'})
    if 1==2:
        rules.append({'低开长阳', 'rule2'})
#end of "def"


def rule_2(code):
    收pre = 0
    开 = 0
    收 = 0
    
    低开度 = 0.01
    长阳度 = 0.08
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 1:
            continue
        else:
            收pre = min(开, 收)
            开 = x['基K'][0]
            高 = x['基K'][1]
            低 = x['基K'][2]
            收 = x['基K'][3]
            if  (收pre - 开) > 开*低开度 and (收 - 开) > 开*长阳度:
                Anlyoutmap[x['date']] = {'rule2', '低开长阳'}
    #end of "for"

    head = "出现日期\t规则ID\t规则名称\n"
    with open(path_rule_rst + code + "_rule2.txt", 'w') as out:
        out.write(head)
        for (d,x) in Anlyoutmap.items():
            tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
            out.write(tmpstr)
        #end of "for"
    #end of "with"
#end of "def"

    
def rule_1(code):
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        开 = x['基K'][0]
        高 = x['基K'][1]
        低 = x['基K'][2]
        收 = x['基K'][3]
        均5  = x['均'][0]
        均10 = x['均'][1]
        均20 = x['均'][2]
        均30 = x['均'][3]
        均60 = x['均'][4]
        if 高>=均5 and 高>=均10 and 高>=均20 and 高>=均30 and 高>=均60 and \
           低<=均5 and 低<=均10 and 低<=均20 and 低<=均30 and 低<=均60:
            Anlyoutmap[x['date']] = {'rule1', '一阳穿五线'} 
    #end of "for"

    head = "出现日期\t规则ID\t规则名称\n"
    with open(path_rule_rst + code + "_rule1.txt", 'w') as out:
        out.write(head)
        for (d,x) in Anlyoutmap.items():
            tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
            out.write(tmpstr)
        #end of "for"
    #end of "with"
#end of "def"


'''进行数据分析'''
def mdl_ruleanlys(code):
    rule_1(code)
    rule_2(code)
#end of "def"


#main()
#获取*.txt，并遍历
files = os.listdir(path_data_avg)
for file in files:
    if file.find("_avg.txt") > 0 or file.find("_avg.TXT") > 0:
        if len(file) == 14:
            code = file[:6]
            mdl_read(code)
            mdl_ruleget(code)
            mdl_ruleanlys(code)
            print(file)
#end of "for"
print("rules分析完毕！\n")



