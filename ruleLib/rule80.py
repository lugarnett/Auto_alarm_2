# -*- coding: utf-8 -*-
import gl
import collections
#import os
Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()
rulen = 'rule80'
Anly_days = gl.Anly_days_80

'''10日线走平'''
'''往前倒推：-1~-19,共20个振幅平
            -22~-25有均线级差
            -27~-34有涨停'''
def rule_80(code, Anlyinmap):
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
        
    振幅 = 0.02
    cnt = 0
    Anlyoutmap.clear()
        
    #遍历
    for (d,x) in Anlymdymap.items():
        flag1 = 0
        flag2 = 0
        flag3 = 0
        
        if d <= 34:
            continue
        else:
            xpre1 = Anlymdymap[d-1]
            xpre2 = Anlymdymap[d-2]
            xpre3 = Anlymdymap[d-3]
            xpre4 = Anlymdymap[d-4]
            xpre5 = Anlymdymap[d-5]
            xpre6 = Anlymdymap[d-6]
            xpre7 = Anlymdymap[d-7]
            xpre8 = Anlymdymap[d-8]
            xpre9 = Anlymdymap[d-9]
            xpre10 = Anlymdymap[d-10]
            xpre11 = Anlymdymap[d-11]
            xpre12 = Anlymdymap[d-12]
            xpre13 = Anlymdymap[d-13]
            xpre14 = Anlymdymap[d-14]
            xpre15 = Anlymdymap[d-15]
            xpre16 = Anlymdymap[d-16]
            xpre17 = Anlymdymap[d-17]
            xpre18 = Anlymdymap[d-18]
            xpre19 = Anlymdymap[d-19]
            xpre20 = Anlymdymap[d-20]
            xpre21 = Anlymdymap[d-21]
            xpre22 = Anlymdymap[d-22]
            xpre23 = Anlymdymap[d-23]
            xpre24 = Anlymdymap[d-24]
            xpre25 = Anlymdymap[d-25]
            xpre26 = Anlymdymap[d-26]
            xpre27 = Anlymdymap[d-27]
            xpre28 = Anlymdymap[d-28]
            xpre29 = Anlymdymap[d-29]
            xpre30 = Anlymdymap[d-30]
            xpre31 = Anlymdymap[d-31]
            xpre32 = Anlymdymap[d-32]
            xpre33 = Anlymdymap[d-33]
            xpre34 = Anlymdymap[d-34]
            xpre35 = Anlymdymap[d-35]

            x1 = xpre1['均'][1]
            x2 = xpre2['均'][1]
            x3 = xpre3['均'][1]
            x4 = xpre4['均'][1]
            x5 = xpre5['均'][1]
            x6 = xpre6['均'][1]
            x7 = xpre7['均'][1]
            x8 = xpre8['均'][1]
            x9 = xpre9['均'][1]
            x10 = xpre10['均'][1]
            x11 = xpre11['均'][1]
            x12 = xpre12['均'][1]
            x13 = xpre13['均'][1]
            x14 = xpre14['均'][1]
            x15 = xpre15['均'][1]
            x16 = xpre16['均'][1]
            x17 = xpre17['均'][1]
            x18 = xpre18['均'][1]
            x19 = xpre19['均'][1]
                        
            高 = x['均'][1] * (1+振幅)
            低 = x['均'][1] * (1-振幅)
            
            '''（1）20天10日均线振幅小于1.7%， 注意量堆，前期有涨停，不破涨停'''
            if x1 < 高 and x1  > 低 and \
            x2 < 高 and x2  > 低 and \
            x3 < 高 and x3  > 低 and \
            x4 < 高 and x4  > 低 and \
            x5 < 高 and x5  > 低 and \
            x6 < 高 and x6  > 低 and \
            x7 < 高 and x7  > 低 and \
            x8 < 高 and x8  > 低 and \
            x9 < 高 and x9  > 低 and \
            x10 < 高 and x10  > 低 and \
            x11 < 高 and x11  > 低 and \
            x12 < 高 and x12  > 低 and \
            x13 < 高 and x13  > 低 and \
            x14 < 高 and x14  > 低 and \
            x15 < 高 and x15  > 低 and \
            x16 < 高 and x16  > 低 and \
            x17 < 高 and x17  > 低 and \
            x18 < 高 and x18  > 低 and \
            x19 < 高 and x19  > 低:
                flag1 = 1
            #endof 'if'    
                
            '''（2）平台前3-6（-19-3~-19-6）天有均线级差'''
            x22_5  = xpre22['均'][0]
            x22_10 = xpre22['均'][1]
            x22_20 = xpre22['均'][2]
            x22_30 = xpre22['均'][3]
            x22_60 = xpre22['均'][4]
            x23_5  = xpre23['均'][0]
            x23_10 = xpre23['均'][1]
            x23_20 = xpre23['均'][2]
            x23_30 = xpre23['均'][3]
            x23_60 = xpre23['均'][4]
            x24_5  = xpre24['均'][0]
            x24_10 = xpre24['均'][1]
            x24_20 = xpre24['均'][2]
            x24_30 = xpre24['均'][3]
            x24_60 = xpre24['均'][4]
            x25_5  = xpre25['均'][0]
            x25_10 = xpre25['均'][1]
            x25_20 = xpre25['均'][2]
            x25_30 = xpre25['均'][3]
            x25_60 = xpre25['均'][4]
            if  x22_5 > x22_10 and x22_10 > x22_20 and x22_20 > x22_30 and x22_30 > x22_60 and \
            (x22_10 - x22_20) > 0.5*(x22_5 - x22_10) and (x22_10 - x22_20) < 2.0*(x22_5 - x22_10) and \
            (x22_20 - x22_30) > 0.5*(x22_10 - x22_20) and (x22_20 - x22_30) < 2.0*(x22_10 - x22_20) and \
            (x22_30 - x22_60) > 0.5*(x22_20 - x22_30) and (x22_30 - x22_60) < 2.0*(x22_20 - x22_30):
                flag2 = flag2 + 1
            if  x23_5 > x23_10 and x23_10 > x23_20 and x23_20 > x23_30 and x23_30 > x23_60 and \
            (x23_10 - x23_20) > 0.5*(x23_5 - x23_10) and (x23_10 - x23_20) < 2.0*(x23_5 - x23_10) and \
            (x23_20 - x23_30) > 0.5*(x23_10 - x23_20) and (x23_20 - x23_30) < 2.0*(x23_10 - x23_20) and \
            (x23_30 - x23_60) > 0.5*(x23_20 - x23_30) and (x23_30 - x23_60) < 2.0*(x23_20 - x23_30):
                flag2 = 1
            if  x24_5 > x24_10 and x24_10 > x24_20 and x24_20 > x24_30 and x24_30 > x24_60 and \
            (x24_10 - x24_20) > 0.5*(x24_5 - x24_10) and (x24_10 - x24_20) < 2.0*(x24_5 - x24_10) and \
            (x24_20 - x24_30) > 0.5*(x24_10 - x24_20) and (x24_20 - x24_30) < 2.0*(x24_10 - x24_20) and \
            (x24_30 - x24_60) > 0.5*(x24_20 - x24_30) and (x24_30 - x24_60) < 2.0*(x24_20 - x24_30):
                flag2 = flag2 + 1
            if  x25_5 > x25_10 and x25_10 > x25_20 and x25_20 > x25_30 and x25_30 > x25_60 and \
            (x25_10 - x25_20) > 0.5*(x25_5 - x25_10) and (x25_10 - x25_20) < 2.0*(x25_5 - x25_10) and \
            (x25_20 - x25_30) > 0.5*(x25_10 - x25_20) and (x25_20 - x25_30) < 2.0*(x25_10 - x25_20) and \
            (x25_30 - x25_60) > 0.5*(x25_20 - x25_30) and (x25_30 - x25_60) < 2.0*(x25_20 - x25_30):
                flag2 = flag2 + 1
            
            
            '''（3）平台前8-15（-19-8~-19-15）天有涨停'''
            收27 = xpre27['基K'][3]
            收28 = xpre28['基K'][3]
            收29 = xpre29['基K'][3]
            收30 = xpre30['基K'][3]
            收31 = xpre31['基K'][3]
            收32 = xpre32['基K'][3]
            收33 = xpre33['基K'][3]
            收34 = xpre34['基K'][3]
            收35 = xpre35['基K'][3]
            if 收34 >= round(收35*1.1,2) or \
            收33 >= round(收34*1.1,2) or \
            收32 >= round(收33*1.1,2) or \
            收31 >= round(收32*1.1,2) or \
            收30 >= round(收31*1.1,2) or \
            收29 >= round(收30*1.1,2) or \
            收28 >= round(收29*1.1,2) or \
            收27 >= round(收28*1.1,2) :
                flag3 = 1
            #endof 'if'
            
            '''（4）'''
            if flag1>=1 and flag2>=1 and flag3>=1:
                Anlyoutmap[x['date']] = [rulen, '10日均线走平（涨停平台整理）']
                Anlyoutmap[xpre1['date']] = ['rule0', '++']
                Anlyoutmap[xpre2['date']] = ['rule0', '++']
                Anlyoutmap[xpre3['date']] = ['rule0', '++']
                Anlyoutmap[xpre4['date']] = ['rule0', '++']
                Anlyoutmap[xpre5['date']] = ['rule0', '++']
                Anlyoutmap[xpre6['date']] = ['rule0', '++']
                Anlyoutmap[xpre7['date']] = ['rule0', '++']
                Anlyoutmap[xpre8['date']] = ['rule0', '++']
                Anlyoutmap[xpre9['date']] = ['rule0', '++']
                Anlyoutmap[xpre10['date']] = ['rule0', '++']
                Anlyoutmap[xpre11['date']] = ['rule0', '++']
                Anlyoutmap[xpre12['date']] = ['rule0', '++']
                Anlyoutmap[xpre13['date']] = ['rule0', '++']
                Anlyoutmap[xpre14['date']] = ['rule0', '++']
                Anlyoutmap[xpre15['date']] = ['rule0', '++']
                Anlyoutmap[xpre16['date']] = ['rule0', '++']
                Anlyoutmap[xpre17['date']] = ['rule0', '++']
                Anlyoutmap[xpre18['date']] = ['rule0', '++']
                Anlyoutmap[xpre19['date']] = ['rule0', '++']
                Anlyoutmap[xpre20['date']] = ['rule0', '++']
                Anlyoutmap[xpre21['date']] = ['rule0', '++']
                Anlyoutmap[xpre22['date']] = ['rule0', '++']
                Anlyoutmap[xpre23['date']] = ['rule0', '++']
                Anlyoutmap[xpre24['date']] = ['rule0', '++']
                Anlyoutmap[xpre25['date']] = ['rule0', '++']
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
