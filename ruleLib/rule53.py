# -*- coding: utf-8 -*-
import gl
import collections
#import os

Anlyoutmap = collections.OrderedDict()  
rulen = 'rule53'

上影度 = 1.04 
短体度 = 1.02

'''大空中加油（短体双上影）'''
def rule_53(code, Anlyinmap):
    global Anlyoutmap
    
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 19:
            continue
        else:
            
            #1)最近一天涨停突破
            收pre1 = Anlyinmap[d-1]['基K'][3]
            收 = Anlyinmap[d]['基K'][3]
            if 收 < round(1.1*收pre1, 2):
                continue
            else:
                最高值 = 收 #涨停值
                
            #2)-1~-19天都小于涨停值，并找出两个次大值d
            f_fail = 0
            次高1 = 0
            次高2 = 0
            次高3 = 0
            次高1day = 0
            次高2day = 0
            次高3day = 0
            for i in range(1, 20):
                tmp高 = Anlyinmap[d-i]['基K'][1]
                if tmp高 > 最高值:
                    f_fail = 1
                    break
                #end if
                if tmp高 > 次高1:
                    次高3 = 次高2
                    次高3day = 次高2day
                    次高2 = 次高1
                    次高2day = 次高1day
                    次高1 = tmp高
                    次高1day = d-i
                elif tmp高 > 次高2:
                    次高3 = 次高2
                    次高3day = 次高2day
                    次高2 = tmp高
                    次高2day = d-i
                elif tmp高 > 次高3:
                    次高3 = tmp高
                    次高3day = d-i
                #endof 'if'
            #endof 'for'
            if f_fail == 1:
                continue
            
            #3)三天里有两天是短2%体+4%上影
            开1 = Anlyinmap[次高1day]['基K'][0]
            高1 = Anlyinmap[次高1day]['基K'][1]
            收1 = Anlyinmap[次高1day]['基K'][3]
            开2 = Anlyinmap[次高2day]['基K'][0]
            高2 = Anlyinmap[次高2day]['基K'][1]
            收2 = Anlyinmap[次高2day]['基K'][3]
            开3 = Anlyinmap[次高3day]['基K'][0]
            高3 = Anlyinmap[次高3day]['基K'][1]
            收3 = Anlyinmap[次高3day]['基K'][3]
            cnt = 0
            if 高1 > 上影度*max(开1,收1) and max(开1,收1) < 短体度*min(开1,收1):
                cnt = cnt + 1
            if 高2 > 上影度*max(开2,收2) and max(开2,收2) < 短体度*min(开2,收2):
                cnt = cnt + 1
            if 高3 > 上影度*max(开3,收3) and max(开3,收3) < 短体度*min(开3,收3):
                cnt = cnt + 1
            if cnt < 2:
                continue
            
            #4)三天里高点均>ma5(?????????????????????????????????????)
            f_succ = 0
            均51 = Anlyinmap[次高1day]['均'][0]
            均52 = Anlyinmap[次高2day]['均'][0]
            均53 = Anlyinmap[次高3day]['均'][0]
            if 高1 > 均51 and 高2 > 均52 and 高3 > 均53 :
                f_succ = 1
            
            
            if f_succ == 1: 
                Anlyoutmap[Anlyinmap[d]['date']] = [rulen, '大空中加油（双上影）']
                #for i in range(min(次高1day,次高2day,次高3day), max(次高1day,次高2day,次高3day)):
                #    Anlyoutmap[Anlyinmap[i]['date']] = ['rule0', '++']
                Anlyoutmap[Anlyinmap[次高1day]['date']] = ['rule0', '++']
                Anlyoutmap[Anlyinmap[次高2day]['date']] = ['rule0', '++']
                Anlyoutmap[Anlyinmap[次高3day]['date']] = ['rule0', '++']
                
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
