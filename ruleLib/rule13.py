# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
rulen = 'rule13'

'''涨停包长阴（上涨过程）'''
def rule_13(code, Anlyinmap):
    global Anlyoutmap
    
    长阴度 = 0.93
    #光脚度 = 1.005
    涨停度 = 1.098
    开盘长阳度 = 1.12
    
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 2:
            continue
        else:
            xpre2 = Anlyinmap[d-2]
            xpre1 = Anlyinmap[d-1]

            收pre2 = xpre2['基K'][3]
            
            开pre1 = xpre1['基K'][0]
            高pre1 = xpre1['基K'][1]
            低pre1 = xpre1['基K'][2]
            收pre1 = xpre1['基K'][3]
            量pre1 = xpre1['V'][0]
            
            开 = x['基K'][0]
            高 = x['基K'][1]
            收 = x['基K'][3]
            量 = x['V'][0]
            
            #第一日跌7%，后面再考虑光脚
            #涨停
            if 收pre1 < 长阴度*max(收pre2,开pre1) \
            and (收 >= round(涨停度*收pre1, 2) or 收 > 开盘长阳度*开):
                Anlyoutmap[x['date']] = [rulen, '涨停包长阴']
                Anlyoutmap[xpre1['date']] = ['rule0', '++']
                cnt = cnt + 1

            #endof 'if'
    #end of "for"

    if cnt > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + "_" + rulen + ".txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
