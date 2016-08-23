# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
Anly_days = gl.Anly_days_5

'''E长下影5'''
def rule_5(code, Anlyinmap):
    global Anlyoutmap,Anlymdymap,Anly_days
    
    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
    
    下影度 = 0.05
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        if d <= -1:
            continue
        else:
            开 = x['基K'][0]
            #高 = x['基K'][1]
            低 = x['基K'][2]
            收 = x['基K'][3]
            if  (min(开,收) - 低) > 开*下影度:
                Anlyoutmap[x['date']] = ['rule5', '长下影5']
                cnt = cnt + 1
            #endof 'if'
    #end of "for"

    if cnt > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + "_rule5.txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
