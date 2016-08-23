# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict() 
Anlymdymap = collections.OrderedDict()  
rulen = 'rule19'
Anly_days = gl.Anly_days_19

'''日内短体上下影2.5%洗盘(1.5%：+—2.5%)'''
def rule_19(code, Anlyinmap):
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
        
    短体度 = 0.015
    上下影度0 = 1.025

    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        if d <= -1:
            continue
        else:
            开 = x['基K'][0]
            高 = x['基K'][1]
            低 = x['基K'][2]
            收 = x['基K'][3]
            
            体长 = max(开,收)/min(开,收) - 1
            上下影度1 = 体长*2.5 + 1
            
            if (体长 < 短体度) \
            and min(开,收) > 上下影度0*低 and min(开,收) > 上下影度1*低 \
            and 高 > 上下影度0*max(开,收) and 高 > 上下影度1*max(开,收):
                Anlyoutmap[x['date']] = [rulen, '日内短体上下影2.5%洗盘']
                cnt = cnt + 1
            #endof 'if'
    #end of "for"

    if cnt > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + '_'+rulen+'.txt', 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
