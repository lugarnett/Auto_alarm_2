# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
Anly_days = gl.Anly_days_62
rulen = 'rule62'

'''7天K线平（当日振幅<3%，价格偏离<1.5%）'''
def rule_62(code, Anlyinmap):

    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
    
    振幅 = 1.03
    偏离 = 1.015
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        #d从0开始
        if d <= 5:
            continue
        else:
            xpre6 = Anlymdymap[d-6]
            xpre5 = Anlymdymap[d-5]
            xpre4 = Anlymdymap[d-4]
            xpre3 = Anlymdymap[d-3]
            xpre2 = Anlymdymap[d-2]
            xpre1 = Anlymdymap[d-1]

            开pre6 = xpre6['基K'][0]
            收pre6 = xpre6['基K'][3]
            
            开pre5 = xpre5['基K'][0]
            收pre5 = xpre5['基K'][3]
            
            开pre4 = xpre4['基K'][0]
            收pre4 = xpre4['基K'][3]
            
            开pre3 = xpre3['基K'][0]
            收pre3 = xpre3['基K'][3]
            
            开pre2 = xpre2['基K'][0]
            收pre2 = xpre2['基K'][3]
            
            开pre1 = xpre1['基K'][0]
            收pre1 = xpre1['基K'][3]
            
            开 = x['基K'][0]
            收 = x['基K'][3]
            
            价pre6 = 0.5*(开pre6 + 收pre6)
            价pre5 = 0.5*(开pre5 + 收pre5)
            价pre4 = 0.5*(开pre4 + 收pre4)
            价pre3 = 0.5*(开pre3 + 收pre3)
            价pre2 = 0.5*(开pre2 + 收pre2)
            价pre1 = 0.5*(开pre1 + 收pre1)
            价 = 0.5*(开 + 收)
            
            if max(开pre6,收pre6) < 振幅*min(开pre6,收pre6) and \
            max(开pre5,收pre5) < 振幅*min(开pre5,收pre5) and \
            max(开pre4,收pre4) < 振幅*min(开pre4,收pre4) and \
            max(开pre3,收pre3) < 振幅*min(开pre3,收pre3) and \
            max(开pre2,收pre2) < 振幅*min(开pre2,收pre2) and \
            max(开pre1,收pre1) < 振幅*min(开pre1,收pre1) and \
            max(开,收) < 振幅*min(开,收) and \
            max(价pre6,价) < 偏离*min(价pre6,价) and \
            max(价pre5,价) < 偏离*min(价pre5,价) and \
            max(价pre4,价) < 偏离*min(价pre4,价) and \
            max(价pre3,价) < 偏离*min(价pre3,价) and \
            max(价pre2,价) < 偏离*min(价pre2,价) and \
            max(价pre1,价) < 偏离*min(价pre1,价) :
                 
                Anlyoutmap[x['date']] = [rulen, '7天K线平（当日振幅<3%，价格偏离<1.5%）']
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
