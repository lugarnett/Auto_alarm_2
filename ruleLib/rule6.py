# -*- coding: utf-8 -*-
import gl
import collections

'''S穿任意4线'''
Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
Anly_days = gl.Anly_days_6

def rule_6(code, Anlyinmap):
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
        
    cnt1 = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        开 = x['基K'][0]
        高 = x['基K'][1]
        低 = x['基K'][2]
        收 = x['基K'][3]
        均5  = x['均'][0]
        均10 = x['均'][1]
        均20 = x['均'][2]
        均30 = x['均'][3]
        均60 = x['均'][4]
        
        #不是5%大跌
        #穿4线
        if not (开-收) > 0.05*收:
            if (高>=均5 and 高>=均10 and 高>=均20 and 高>=均30 and 低<=均5 and 低<=均10 and 低<=均20 and 低<=均30) and not (高>=均60 and 低<=均60):
                Anlyoutmap[x['date']] = ['rule6', '穿任意4线'] 
                cnt1 = cnt1 + 1
            elif (高>=均5 and 高>=均10 and 高>=均20 and 高>=均60 and 低<=均5 and 低<=均10 and 低<=均20 and 低<=均60) and not (高>=均30 and 低<=均30):
                Anlyoutmap[x['date']] = ['rule6', '穿任意4线'] 
                cnt1 = cnt1 + 1
            elif (高>=均5 and 高>=均10 and 高>=均60 and 高>=均30 and 低<=均5 and 低<=均10 and 低<=均60 and 低<=均30) and not (高>=均20 and 低<=均20):
                Anlyoutmap[x['date']] = ['rule6', '穿任意4线'] 
                cnt1 = cnt1 + 1   
            elif (高>=均5 and 高>=均60 and 高>=均20 and 高>=均30 and 低<=均5 and 低<=均60 and 低<=均20 and 低<=均30) and not (高>=均10 and 低<=均10):
                Anlyoutmap[x['date']] = ['rule6', '穿任意4线'] 
                cnt1 = cnt1 + 1
            elif (高>=均60 and 高>=均10 and 高>=均20 and 高>=均30 and 低<=均60 and 低<=均10 and 低<=均20 and 低<=均30) and not (高>=均5 and 低<=均5):
                Anlyoutmap[x['date']] = ['rule6', '穿任意4线'] 
                cnt1 = cnt1 + 1
        #endof 'if'
    #end of "for"

    if cnt1 > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + "_rule6.txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
