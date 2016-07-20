# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
rulen = 'rule16'

'''瘦长十字星（涨停后），最好是涨停启动后（价格和涨停价一致）！！'''
def rule_16(code, Anlyinmap):
    global Anlyoutmap
    
    上影度 = 1.03
    下影度 = 0.97
    短体度 = 1.005
    
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
            
            if max(开,收) < 短体度*min(开,收) \
            and 高 > 上影度*max(开,收) and 低 < 下影度*min(开,收):
                Anlyoutmap[x['date']] = [rulen, '瘦长十字星（涨停后？？）']
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
