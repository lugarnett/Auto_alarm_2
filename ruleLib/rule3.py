# -*- coding: utf-8 -*-
import gl

import collections
import os

Anlyoutmap = collections.OrderedDict()  

'''涨停且有1%下影或低开'''
def rule_3(code, Anlyinmap):
    收pre = 0
    开 = 0
    收 = 0
    
    低开度 = 0.01
    涨停度 = 1.098
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 1:
            continue
        else:
            收pre = 收
            开 = x['基K'][0]
            高 = x['基K'][1]
            低 = x['基K'][2]
            收 = x['基K'][3]
            if 收 >= round(涨停度*收pre, 2):
                if  (收pre-开) > 开*低开度 or (低-开) > 开*低开度:
                    Anlyoutmap[x['date']] = ['rule3', '涨停且有1%下影或低开']
                    cnt = cnt + 1
                #endof 'if'
            #endof 'if'
    #end of "for"

    if cnt > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + "_rule3.txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
