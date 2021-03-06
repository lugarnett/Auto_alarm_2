# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
Anly_days = gl.Anly_days_7

'''量价红三兵'''
def rule_7(code, Anlyinmap):

    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
        
    开 = 0
    收 = 0
    量 = 0
    
    长阳度 = 0.015
    量增 = 1.4
    cnt2 = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        #d从0开始
        if d <= 1:
            continue
        else:
            xpre2 = Anlymdymap[d-2]
            xpre1 = Anlymdymap[d-1]
 
            开pre2 = xpre2['基K'][0]
            收pre2 = xpre2['基K'][3]
            量pre2 = xpre2['V'][0]
            
            开pre1 = xpre1['基K'][0]
            收pre1 = xpre1['基K'][3]
            量pre1 = xpre1['V'][0]
            
            开 = x['基K'][0]
            收 = x['基K'][3]
            量 = x['V'][0]
            
            if (收-开) > 开*长阳度 and \
            (收pre1-开pre1) > 开pre1*长阳度 and \
            (收pre2-开pre2) > 开pre2*长阳度 and \
            量 > 量增*量pre1 and \
            量pre1 > 量增*量pre2:
                 
                Anlyoutmap[xpre2['date']] = ['rule7', '量价红三兵']
                Anlyoutmap[xpre1['date']] = ['rule0', '++']
                Anlyoutmap[x['date']] = ['rule0', '++']
                cnt2 = cnt2 + 1
            #endof 'if'
    #end of "for"

    if cnt2 > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + "_rule7.txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
