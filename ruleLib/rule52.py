# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
rulen = 'rule52'

上影度 = 1.06 

'''大空中加油（涨停加上影加涨停）'''
def rule_52(code, Anlyinmap):
    global Anlyoutmap
    
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 14:
            continue
        else:
            
            #1)最近一天涨停突破
            收pre1 = Anlyinmap[d-1]['基K'][3]
            收 = Anlyinmap[d]['基K'][3]
            if 收 < round(1.1*收pre1, 2):
                continue
            else:
                最高值 = 收 #涨停值
                
            #2)-1~-13天都小于涨停值，并找出两个次大值d
            f_fail = 0
            次高1 = 0
            次高2 = 0
            次高1day = 0
            次高2day = 0
            for i in range(1, 14):
                tmp高 = Anlyinmap[d-i]['基K'][1]
                if tmp高 > 最高值:
                    f_fail = 1
                    break
                #end if
                if tmp高 > 次高1:
                    次高2 = 次高1
                    次高2day = 次高1day
                    次高1 = tmp高
                    次高1day = d-i
                elif tmp高 > 次高2:
                    次高2 = tmp高
                    次高2day = d-i
                #endof 'if'
            #endof 'for'
            if f_fail == 1:
                continue
            
            #3)两天里有一天是上影
            开1 = Anlyinmap[次高1day]['基K'][0]
            高1 = Anlyinmap[次高1day]['基K'][1]
            收1 = Anlyinmap[次高1day]['基K'][3]
            开2 = Anlyinmap[次高2day]['基K'][0]
            高2 = Anlyinmap[次高2day]['基K'][1]
            收2 = Anlyinmap[次高2day]['基K'][3]
            if not (高1 > 上影度*max(开1,收1) or 高2 > 上影度*max(开2,收2)):
                continue
            
            #4)两天里高点均>ma5(?????????????????????????????????????)
            均51 = Anlyinmap[次高1day]['均'][0]
            均52 = Anlyinmap[次高2day]['均'][0]
            if not (高1 > 均51 and 高2 > 均52):
                continue
            
            #5)-14~次高day天有涨停值，涨停值小于次高1day收 & 次高2day收
            次高1day收 = 收1
            次高2day收 = 收2
            f_succ = 0
            for i in range(d-14, min(次高1day,次高2day)):
                tmp开 = Anlyinmap[i]['基K'][0]
                tmp收 = Anlyinmap[i]['基K'][3]
                if tmp收 >= round(1.1*tmp开, 2) and tmp收 < 次高1day收 and tmp收 < 次高2day收:
                    f_succ = 1
                    涨停启动day = i
                    break
                #endof 'if'
            #endof 'for'
            
            
            if f_succ == 1: 
                Anlyoutmap[Anlyinmap[d]['date']] = [rulen, '大空中加油（涨停加上影加涨停）']
                #for i in range(涨停启动day, max(次高1day,次高2day)):
                #    Anlyoutmap[Anlyinmap[i]['date']] = ['rule0', '++']
                Anlyoutmap[Anlyinmap[涨停启动day]['date']] = ['rule0', '++']
                Anlyoutmap[Anlyinmap[次高1day]['date']] = ['rule0', '++']
                Anlyoutmap[Anlyinmap[次高2day]['date']] = ['rule0', '++']
                    
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
