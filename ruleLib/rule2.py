# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()
Anlymdymap = collections.OrderedDict()    
Anly_days = gl.Anly_days_2

'''低开长阳（板寸）'''
def rule_2(code, Anlyinmap):
    
    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
        
    收pre = 0
    开 = 0
    收 = 0
    
    低开度 = 0.015
    长阳度 = 0.07
    板寸度 = 1.005
    cnt2 = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        if d <= -1:
            continue
        else:
            收pre = min(开, 收)
            开 = x['基K'][0]
            高 = x['基K'][1]
            低 = x['基K'][2]
            收 = x['基K'][3]
            if  (收pre-开) > 开*低开度 and (收-开) > 开*长阳度 and 高 <= 板寸度*收: # 板寸接近光头阳:
                Anlyoutmap[x['date']] = ['rule2', '低开长阳']
                cnt2 = cnt2 + 1
            #endof 'if'
    #end of "for"

    if cnt2 > 0:
        head = "出现日期\t规则ID\t规则名称\n"
        with open(gl.path_rule_rst + code + "_rule2.txt", 'w') as out:
            out.write(head)
            for (d,x) in Anlyoutmap.items():
                tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
                out.write(tmpstr)
            #end of "for"
        #end of "with"
    #endof 'if'
#end of "def"
