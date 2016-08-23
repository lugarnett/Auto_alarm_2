# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()
rulen = 'rule15'
Anly_days = gl.Anly_days_15

'''跳空巨量中阴不回，第二天长阳（最好高开）'''
def rule_15(code, Anlyinmap):
    global Anlyoutmap,Anlymdymap,rulen,Anly_days

    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
            
    巨量度 = 1.3
    中阴度 = 0.97
    长阳度 = 1.07
    #光脚度 = 1.005
    
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        if d <= 1:
            continue
        else:
            xpre2 = Anlymdymap[d-2]
            xpre1 = Anlymdymap[d-1]

            高pre2 = xpre2['基K'][1]
            量pre2 = xpre2['V'][0]
            
            开pre1 = xpre1['基K'][0]
            高pre1 = xpre1['基K'][1]
            低pre1 = xpre1['基K'][2]
            收pre1 = xpre1['基K'][3]
            量pre1 = xpre1['V'][0]
            
            开 = x['基K'][0]
            高 = x['基K'][1]
            低 = x['基K'][2]
            收 = x['基K'][3]
            量 = x['V'][0]
            
            #第一天跳空巨量中阴
            #第一天7%长阳
            #两天最低均不回前一天的高\低（收）
            if 收pre1 < 中阴度*开pre1 and 低pre1 > 高pre2 and 量pre1 > 巨量度*量pre2\
            and 收 > 长阳度*开 and 低 >= 低pre1:
                Anlyoutmap[x['date']] = [rulen, '跳空中阴不回，第二天长阳（最好高开）']
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
