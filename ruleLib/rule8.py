# -*- coding: utf-8 -*-
import gl

import collections
import os

Anlyoutmap = collections.OrderedDict()  

'''红二三兵穿五线'''
def rule_8(code, Anlyinmap):
    收pre = 0
    量pre = 0
    开 = 0
    收 = 0
    量 = 0
    
    涨幅 = 1.09
    量增 = 1.4
    cnt2 = 0
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 2:
            continue
        else:
            xpre2 = Anlyinmap[d-2]
            xpre1 = Anlyinmap[d-1]
 
            开pre2 = xpre2['基K'][0]
            收pre2 = xpre2['基K'][3]
            均5pre2  = xpre2['均'][0]
            均10pre2 = xpre2['均'][1]
            均20pre2 = xpre2['均'][2]
            均30pre2 = xpre2['均'][3]
            均60pre2 = xpre2['均'][4]
            量pre2 = xpre2['V'][0]
            
            开pre1 = xpre1['基K'][0]
            收pre1 = xpre1['基K'][3]
            均5pre1  = xpre1['均'][0]
            均10pre1 = xpre1['均'][1]
            均20pre1 = xpre1['均'][2]
            均30pre1 = xpre1['均'][3]
            均60pre1 = xpre1['均'][4]
            量pre1 = xpre1['V'][0]
            
            开 = x['基K'][0]
            高 = x['基K'][1]
            低 = x['基K'][2]
            收 = x['基K'][3]
            均5  = x['均'][0]
            均10 = x['均'][1]
            均20 = x['均'][2]
            均30 = x['均'][3]
            均60 = x['均'][4]
            量 = x['V'][0]
            
            #两阳
            #三天穿均线
            #后两天有涨停|长阳（含跳空）
            #三天有放量
            if (收>开) and (收pre1>开pre1):
                if 开pre2<均5pre2 and 开pre2<均10pre2 and 开pre2<均20pre2 and \
                开pre2<均30pre2 and 开pre2<均60pre2 and \
                收>均5 and 收>均10 and 收>均20 and 收>均30 and 收>均60:
                    if 收>(涨幅*收pre1) or 收pre1>(涨幅*收pre2):
                        if 量>量增*量pre1 or 量pre1>量增*量pre2:
                            Anlyoutmap[x['date']] = ['rule8', '红三兵穿五线']
                            cnt2 = cnt2 + 1
                        #endof 'if'
                    #endof 'if'
                #endof 'if'
            #endof 'if'
    #end of "for"

    if cnt2 > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + "_rule8.txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
