# -*- coding: utf-8 -*-
import gl
import collections
#import os
Anlyoutmap = collections.OrderedDict()  

rulen = 'rule80'

'''10日线走平'''
def rule_80(code, Anlyinmap):
    global rulen
    
    振幅 = 0.03
    cnt = 0
    Anlyoutmap.clear()
    
    #遍历
    for (d,x) in Anlyinmap.items():
        if d <= 20:
            continue
        else:
            x1 = Anlyinmap[d-1]['均'][1]
            x2 = Anlyinmap[d-2]['均'][1]
            x3 = Anlyinmap[d-3]['均'][1]
            x4 = Anlyinmap[d-4]['均'][1]
            x5 = Anlyinmap[d-5]['均'][1]
            x6 = Anlyinmap[d-6]['均'][1]
            x7 = Anlyinmap[d-7]['均'][1]
            x8 = Anlyinmap[d-8]['均'][1]
            x9 = Anlyinmap[d-9]['均'][1]
            x10 = Anlyinmap[d-10]['均'][1]
            x11 = Anlyinmap[d-11]['均'][1]
            x12 = Anlyinmap[d-12]['均'][1]
            x13 = Anlyinmap[d-13]['均'][1]
            x14 = Anlyinmap[d-14]['均'][1]
            x15 = Anlyinmap[d-15]['均'][1]
            x16 = Anlyinmap[d-16]['均'][1]
            x17 = Anlyinmap[d-17]['均'][1]
            x18 = Anlyinmap[d-18]['均'][1]
            x19 = Anlyinmap[d-19]['均'][1]
            
            高 = x['均'][1] * (1+振幅)
            低 = x['均'][1] * (1-振幅)
            
            #20天10日均线振幅小于3%
            #注意量堆，前期有涨停，不破涨停
            if x1 < 高 and x1  > 低 and \
            x2 < 高 and x2  > 低 and \
            x3 < 高 and x3  > 低 and \
            x4 < 高 and x4  > 低 and \
            x5 < 高 and x5  > 低 and \
            x6 < 高 and x6  > 低 and \
            x7 < 高 and x7  > 低 and \
            x8 < 高 and x8  > 低 and \
            x9 < 高 and x9  > 低 and \
            x10 < 高 and x10  > 低 and \
            x11 < 高 and x11  > 低 and \
            x12 < 高 and x12  > 低 and \
            x13 < 高 and x13  > 低 and \
            x14 < 高 and x14  > 低 and \
            x15 < 高 and x15  > 低 and \
            x16 < 高 and x16  > 低 and \
            x17 < 高 and x17  > 低 and \
            x18 < 高 and x18  > 低 and \
            x19 < 高 and x19  > 低:
                Anlyoutmap[x['date']] = [rulen, '10日均线走平']
                Anlyoutmap[x1['date']] = ['rule0', '++']
                Anlyoutmap[x2['date']] = ['rule0', '++']
                Anlyoutmap[x3['date']] = ['rule0', '++']
                Anlyoutmap[x4['date']] = ['rule0', '++']
                Anlyoutmap[x5['date']] = ['rule0', '++']
                Anlyoutmap[x6['date']] = ['rule0', '++']
                Anlyoutmap[x7['date']] = ['rule0', '++']
                Anlyoutmap[x8['date']] = ['rule0', '++']
                Anlyoutmap[x9['date']] = ['rule0', '++']
                Anlyoutmap[x10['date']] = ['rule0', '++']
                Anlyoutmap[x11['date']] = ['rule0', '++']
                Anlyoutmap[x12['date']] = ['rule0', '++']
                Anlyoutmap[x13['date']] = ['rule0', '++']
                Anlyoutmap[x14['date']] = ['rule0', '++']
                Anlyoutmap[x15['date']] = ['rule0', '++']
                Anlyoutmap[x16['date']] = ['rule0', '++']
                Anlyoutmap[x17['date']] = ['rule0', '++']
                Anlyoutmap[x18['date']] = ['rule0', '++']
                Anlyoutmap[x19['date']] = ['rule0', '++']
                cnt = cnt + 1
                #endof 'if'
            #endof 'if'
    #end of "for"

    if cnt > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + '_'+rulen+".txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
