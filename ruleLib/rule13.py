# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
rulen = 'rule13'

'''长上影次日高开收阳（最好是大跌后走平）'''
def rule_13(code, Anlyinmap):
    global Anlyoutmap
    
    加下影短体度 = 1.01
    上影度 = 1.06
    #高开度 = 1.01
    
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 1:
            continue
        else:
            xpre1 = Anlyinmap[d-1]

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
            
            #第一日短体长上影
            #高开收阳，最低不破昨日收
            if (max(收pre1,开pre1) < 加下影短体度*min(收pre1,开pre1,低pre1)) and (高pre1 > 上影度*收pre1) \
            and (开 > 收pre1) and (收 > 开) and (低 > 收pre1) :
                Anlyoutmap[x['date']] = [rulen, '长上影次日高开收阳']
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
