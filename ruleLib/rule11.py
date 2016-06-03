# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
rulen = 'rule11'

'''一阳补三阴'''
def rule_11(code, Anlyinmap):
    global Anlyoutmap
    
    长阳度 = 1.02
    
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 4:
            continue
        else:
            xpre4 = Anlyinmap[d-4]
            xpre3 = Anlyinmap[d-3]
            xpre2 = Anlyinmap[d-2]
            xpre1 = Anlyinmap[d-1]
 
            收pre4 = xpre4['基K'][3]
            
            开pre3 = xpre3['基K'][0]
            高pre3 = xpre3['基K'][1]
            收pre3 = xpre3['基K'][3]
            量pre3 = xpre3['V'][0]
            
            开pre2 = xpre2['基K'][0]
            高pre2 = xpre2['基K'][1]
            收pre2 = xpre2['基K'][3]
            量pre2 = xpre2['V'][0]
            
            开pre1 = xpre1['基K'][0]
            高pre1 = xpre1['基K'][1]
            收pre1 = xpre1['基K'][3]
            量pre1 = xpre1['V'][0]
            
            开 = x['基K'][0]
            收 = x['基K'][3]
            量 = x['V'][0]
            
            if (收 > 开*长阳度) and (收 > max(高pre3,高pre2,高pre1)) and (量 > max(量pre3,量pre2,量pre1)) \
            and (收pre3 < 开pre3 or 收pre3 < 收pre4) \
            and (收pre2 < 开pre2 or 收pre2 < 收pre3) \
            and (收pre1 < 开pre1 or 收pre1 < 收pre2) :
                
                Anlyoutmap[xpre3['date']] = ['rule0', '++']
                Anlyoutmap[xpre2['date']] = ['rule0', '++']
                Anlyoutmap[xpre1['date']] = ['rule0', '++']
                Anlyoutmap[x['date']] = [rulen, '一阳补三阴']
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
