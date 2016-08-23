# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()
rulen = 'rule18'
Anly_days = gl.Anly_days_18

'''反上下影洗盘(收盘接近?)'''
def rule_18(code, Anlyinmap):
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
        
    上影度 = 1 + 0.03
    下影度 = 1 - 0.03
    短体度 = 1.02
    
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
            低 = x['基K'][2]
            收 = x['基K'][3]
            量 = x['V'][0]
            
            if max(开,收) < 短体度*min(开,收) and 高 > 上影度*max(开,收) \
            and max(开pre1,收pre1) < 短体度*min(开pre1,收pre1) and 低pre1 < 下影度*min(开pre1,收pre1):
                Anlyoutmap[x['date']] = [rulen, '反上下影洗盘(收盘接近?)']
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
