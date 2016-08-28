# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
Anly_days = gl.Anly_days_65
rulen = 'rule65'

'''4天K线平5日线平（K振幅<1.5%，均偏离<0.5%）'''
def rule_65(code, Anlyinmap):

    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
    
    振幅 = 1.015
    偏离 = 1.005
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        #d从0开始
        if d <= 2:
            continue
        else:
            xpre3 = Anlymdymap[d-3]
            xpre2 = Anlymdymap[d-2]
            xpre1 = Anlymdymap[d-1]

            开pre3 = xpre3['基K'][0]
            收pre3 = xpre3['基K'][3]
            均pre3 = xpre3['均'][0]
            
            开pre2 = xpre2['基K'][0]
            收pre2 = xpre2['基K'][3]
            均pre2 = xpre2['均'][0]
            
            开pre1 = xpre1['基K'][0]
            收pre1 = xpre1['基K'][3]
            均pre1 = xpre1['均'][0]
            
            开 = x['基K'][0]
            收 = x['基K'][3]
            均 = x['均'][0]
            
            if max(开pre3,收pre3) < 振幅*min(开pre3,收pre3) and \
            max(开pre2,收pre2) < 振幅*min(开pre2,收pre2) and \
            max(开pre1,收pre1) < 振幅*min(开pre1,收pre1) and \
            max(开,收) < 振幅*min(开,收) and \
            max(均pre3,均) < 偏离*min(均pre3,均) and \
            max(均pre2,均) < 偏离*min(均pre2,均) and \
            max(均pre1,均) < 偏离*min(均pre1,均) :
                 
                Anlyoutmap[x['date']] = [rulen, '4天K线平5日线平']
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
