# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()
rulen = 'rule12'
Anly_days = gl.Anly_days_12

'''短体（含下影不超3.5%）长上影（大于3.5%），第二天长收回（最好光头长阳）'''
def rule_12(code, Anlyinmap):
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
            
    短体度 = 1.035
    上影度 = 1.035
    #高开度 = 1.01
    长阳度 = 1.07
    光头阳 = 1.005
    
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        if d <= 0:
            continue
        else:
            xpre1 = Anlymdymap[d-1]

            开pre1 = xpre1['基K'][0]
            高pre1 = xpre1['基K'][1]
            低pre1 = xpre1['基K'][2]
            收pre1 = xpre1['基K'][3]
            量pre1 = xpre1['V'][0]
            
            开 = x['基K'][0]
            高 = x['基K'][1]
            收 = x['基K'][3]
            量 = x['V'][0]
            
            #第一日短体上影
            #光头阳
            if max(收pre1,开pre1) < 短体度*min(收pre1,开pre1,低pre1) and (高pre1 > 上影度*收pre1) \
            and 高 < 光头阳*收 \
            and (收 > 高pre1 or 收 > 长阳度*收pre1) :
                Anlyoutmap[x['date']] = [rulen, '短体上影次日高开或收回']
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
