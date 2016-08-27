# -*- coding: utf-8 -*-
import gl
import collections

Anlyoutmap = collections.OrderedDict()  
Anlymdymap = collections.OrderedDict()  
Anly_days = gl.Anly_days_70
rulen = 'rule70'

'''缓拉吸筹(20天),20天内阴线<=4，涨停<=3（有跳空低开,正量多）'''
def rule_70(code, Anlyinmap):

    max_n = max(Anlyinmap.keys())
    days = Anly_days + gl.Anly_days_add
    #天数不够
    if max_n+1 < days: 
        return
    #end if
    for i in range(days):
        Anlymdymap[i] = Anlyinmap[max_n+1 - days + i]
    #end for
    
    cnt = 0
    Anlyoutmap.clear()
    for (d,x) in Anlymdymap.items():
        #d从0开始
        if d <= 19:
            continue
        else:
            cnt_Neg = 0
            cnt_ZT = 0
			
            flag = 1
            for i in range(20):
                xi = Anlymdymap[d-i]
                xipre = Anlymdymap[d-i-1]
        				
                开i = xi['基K'][0]
                收i = xi['基K'][3]
                收ipre = xipre['基K'][3]

                #阴线<=4
                if 收i <= 开i:
                    cnt_Neg = cnt_Neg + 1
                #end if
                if cnt_Neg > 4:
                    flag = 0
                    break
                #end if
                
                #涨停<=3
                if 收i >= round(1.1*收ipre, 2):
                    cnt_ZT = cnt_ZT + 1
                #end if
                if cnt_ZT > 3:
                    flag = 0
                    break
                #end if

                #若无break，则成功找到
            #end for

            if flag == 1:
                Anlyoutmap[x['date']] = [rulen, '缓拉吸筹']
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
