# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
rulen = 'rule12'

'''长上影小阳线，第二天高开，收阳>1%   \或  收>1.04*收per'''
def rule_12(code, Anlyinmap):
    global Anlyoutmap
    
    上影度 = 1.04
    高开度 = 1.01
    长阳度 = 1.01
    
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 2:
            continue
        else:
            xpre1 = Anlyinmap[d-1]

            开pre1 = xpre1['基K'][0]
            高pre1 = xpre1['基K'][1]
            收pre1 = xpre1['基K'][3]
            量pre1 = xpre1['V'][0]
            
            开 = x['基K'][0]
            收 = x['基K'][3]
            量 = x['V'][0]
            
            if (收pre1 > 开pre1) and (高pre1 > 上影度*收pre1) :
                if (开 > 高开度*收pre1 and 收 > 长阳度*开) or (收 > 1.04*收pre1) :
                    Anlyoutmap[x['date']] = [rulen, '上影小阳次日高开或收回']
                    Anlyoutmap[xpre1['date']] = ['rule0', '++']
                    cnt = cnt + 1
                #endof 'if'
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
