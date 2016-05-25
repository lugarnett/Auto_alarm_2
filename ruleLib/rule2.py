# -*- coding: utf-8 -*-
import gl

import collections
import os

Anlyoutmap = collections.OrderedDict()  

'''低开长阳'''
def rule_2(code, Anlyinmap):
    收pre = 0
    开 = 0
    收 = 0
    
    低开度 = 0.015
    长阳度 = 0.07
    cnt2 = 0
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 1:
            continue
        else:
            收pre = min(开, 收)
            开 = x['基K'][0]
            高 = x['基K'][1]
            低 = x['基K'][2]
            收 = x['基K'][3]
            if  (收pre-开) > 开*低开度 and (收-开) > 开*长阳度:# and 收 == 高:
                Anlyoutmap[x['date']] = ['rule2', '低开长阳']
                cnt2 = cnt2 + 1
            #endof 'if'
    #end of "for"

    if cnt2 > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + "_rule2.txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
