# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
rulen = 'rule9'
Anly_days = gl.Anly_days_9

'''连天价跌时无量（最好是十字星）'''
def rule_9(code, Anlyinmap):
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
        
    振幅 = 1.08
    缩量度 = 0.3
    cnt = 0
    Anlyoutmap.clear()

    #遍历
    for (d,x) in Anlymdymap.items():
        if d <= 1:
            continue
        else:
            xpre2 = Anlymdymap[d-2]
            xpre1 = Anlymdymap[d-1]
 
            开pre2 = xpre2['基K'][0]
            收pre2 = xpre2['基K'][3]
            量pre2 = xpre2['V'][0]
            量ma5pre2 = xpre2['V_ma'][0]
            
            开pre1 = xpre1['基K'][0]
            收pre1 = xpre1['基K'][3]
            量pre1 = xpre1['V'][0]
            量ma5pre1 = xpre1['V_ma'][0]
            
            开 = x['基K'][0]
            收 = x['基K'][3]
            量 = x['V'][0]
            
            v_avg = 0.5*(量ma5pre2 + 量ma5pre1)
            #两天，类十字星<8%
            #两天缩量
            if max(收,开)<min(收,收pre1)*振幅 and max(收pre1,开pre1)<min(收pre1,收pre2)*振幅:
                if 量 < v_avg*缩量度 and 量pre1 < v_avg*缩量度:
                    Anlyoutmap[xpre1['date']] = [rulen, '价跌时无量']
                    Anlyoutmap[x['date']] = ['rule0', '++']
                    cnt = cnt + 1
                #endof 'if'
            #endof 'if'
    #end of "for"

    if cnt > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + '_'+rulen+".txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
