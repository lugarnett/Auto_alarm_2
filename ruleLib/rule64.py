# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
Anly_days = gl.Anly_days_64
rulen = 'rule64'

'''7天10日线平（偏离<1.5%）'''
def rule_64(code, Anlyinmap):

    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
    
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

            #均10
            均pre6 = xpre6['均'][1]
            均pre5 = xpre5['均'][1]
            均pre4 = xpre4['均'][1]
            均pre3 = xpre3['均'][1]
            均pre2 = xpre2['均'][1]
            均pre1 = xpre1['均'][1]
            均 = x['均'][1]
            
            if max(均pre6,均) < 偏离*min(均pre6,均) and \
            max(均pre5,均) < 偏离*min(均pre5,均) and \
            max(均pre4,均) < 偏离*min(均pre4,均) and \
            max(均pre3,均) < 偏离*min(均pre3,均) and \
            max(均pre2,均) < 偏离*min(均pre2,均) and \
            max(均pre1,均) < 偏离*min(均pre1,均) :
                 
                Anlyoutmap[x['date']] = [rulen, '7天10日线平（偏离<1.5%）']
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
