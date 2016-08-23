# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()
rulen = 'rule51'
Anly_days = gl.Anly_days_51

'''小空中加油（六天不连续三涨停）'''
def rule_51(code, Anlyinmap):
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
        
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        if d <= 5:
            continue
        else:
            xpre6 = Anlymdymap[d-6]
            xpre5 = Anlymdymap[d-5]
            xpre4 = Anlymdymap[d-4]
            xpre3 = Anlymdymap[d-3]
            xpre2 = Anlymdymap[d-2]
            xpre1 = Anlymdymap[d-1]
 
            收pre6 = xpre6['基K'][3]
            收pre5 = xpre5['基K'][3]
            收pre4 = xpre4['基K'][3]
            收pre3 = xpre3['基K'][3]
            收pre2 = xpre2['基K'][3]
            收pre1 = xpre1['基K'][3]
            
            收 = x['基K'][3]
            
            if (收 < 1.098*收pre1 \
            and 收pre1 >= round(1.098*收pre2, 2) \
            and 收pre2 >= round(1.098*收pre3, 2) \
            and 收pre3 < 1.098*收pre4 \
            and 收pre4 >= round(1.098*收pre5, 2) \
            and 收pre5 < 1.098*收pre6) \
            or (收 < 1.098*收pre1 \
            and 收pre1 >= round(1.098*收pre2, 2) \
            and 收pre2 < 1.098*收pre3 \
            and 收pre3 >= round(1.098*收pre4, 2) \
            and 收pre4 >= round(1.098*收pre5, 2) \
            and 收pre5 < 1.098*收pre6): 
                
                Anlyoutmap[xpre4['date']] = ['rule0', '++']
                Anlyoutmap[xpre3['date']] = ['rule0', '++']
                Anlyoutmap[xpre2['date']] = ['rule0', '++']
                Anlyoutmap[xpre1['date']] = ['rule0', '++']
                Anlyoutmap[x['date']] = [rulen, '小空中加油（六天三涨停）']
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
