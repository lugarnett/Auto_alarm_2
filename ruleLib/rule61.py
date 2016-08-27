# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
Anly_days = gl.Anly_days_61
rulen = 'rule61'

'''连续7连阴'''
def rule_61(code, Anlyinmap):

    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
    
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
            
            if 收pre6 < 开pre6 and \
            收pre5 < 开pre5 and \
            收pre4 < 开pre4 and \
            收pre3 < 开pre3 and \
            收pre2 < 开pre2 and \
            收pre1 < 开pre1 and \
            收 < 开:

                Anlyoutmap[x['date']] = [rulen, '连续7连阴']
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
