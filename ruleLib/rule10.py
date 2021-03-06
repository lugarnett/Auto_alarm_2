# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
rulen = 'rule10'
Anly_days = gl.Anly_days_10

'''跳空1%涨停'''
def rule_10(code, Anlyinmap):
    global Anlyoutmap,Anlymdymap,rulen,Anly_days

    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
        
    跳空度 = 0.01
    涨停度 = 1.099
    收 = 1000
    开 = 1000
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        if d <= -1:
            continue
        else:
            收pre = 收
            昨 = max(收,开)
            开 = x['基K'][0]
            低 = x['基K'][2]
            收 = x['基K'][3]
            if 收 >= round(涨停度*收pre, 2) and 收 > 开:
                if  (低-昨) > 昨*跳空度:
                    Anlyoutmap[x['date']] = [rulen, '跳空1%涨停']
                    cnt = cnt + 1
                #endof 'if'
            #endof 'if'
    #end of "for"

    if cnt > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + "_"+rulen+".txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
