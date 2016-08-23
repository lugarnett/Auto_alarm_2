# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()
rulen = 'rule121'
Anly_days = gl.Anly_days_121

'''n天内有涨停'''
def rule_121(code, Anlyinmap):
    global Anlyoutmap,Anlymdymap,rulen,Anly_days

    max_n = max(Anlyinmap.keys())
    days = Anly_days
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
           
    涨停度 = 1.1
    cnt = 0
    Anlyoutmap.clear()
    
    for (d,x) in Anlymdymap.items():
        if d <= 0:
            continue
        else:
            xpre1 = Anlymdymap[d-1]

            收pre1 = xpre1['基K'][3]
            收 = x['基K'][3]
            
            #涨停
            if 收 >= round(涨停度*收pre1, 2):
                Anlyoutmap[x['date']] = [rulen, '涨停标志']
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
