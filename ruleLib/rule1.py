# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
rulen = 'rule1'
Anly_days = gl.Anly_days_1

'''一阳穿五线,非-3%大跌'''
def rule_1(code, Anlyinmap):
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
    
    cnt1 = 0
    收 = 1000
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        收pre = 收
        开 = x['基K'][0]
        高 = x['基K'][1]
        低 = x['基K'][2]
        收 = x['基K'][3]
        均5  = x['均'][0]
        均10 = x['均'][1]
        均20 = x['均'][2]
        均30 = x['均'][3]
        均60 = x['均'][4]
        
        最低 = min(收pre,低)
        #穿均线
        #不是3%大跌
        if 高>=均5 and 高>=均10 and 高>=均20 and 高>=均30 and 高>=均60 and \
           最低<=均5 and 最低<=均10 and 最低<=均20 and 最低<=均30 and 最低<=均60:
               if not (开-收) > 0.03*收:
                   Anlyoutmap[x['date']] = [rulen, '一阳穿五线']
                   cnt1 = cnt1 + 1
    #end of "for"

    if cnt1 > 0:
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
