# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
rulen = 'rule50'

'''小空中加油（有三必有五）'''
def rule_50(code, Anlyinmap):
    global Anlyoutmap
    
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
            收pre3 = xpre3['基K'][3]
            收pre2 = xpre2['基K'][3]
            收pre1 = xpre1['基K'][3]
            
            收 = x['基K'][3]
            
            if  收 >= round(1.1*收pre1, 2) \
            and 收pre1 >= round(1.1*收pre2, 2) \
            and 收pre2 >= round(1.1*收pre3, 2) \
            and 收pre3 < 1.098*收pre4: 
                
                Anlyoutmap[xpre2['date']] = ['rule0', '++']
                Anlyoutmap[xpre1['date']] = ['rule0', '++']
                Anlyoutmap[x['date']] = [rulen, '小空中加油（有三必有五）']
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
