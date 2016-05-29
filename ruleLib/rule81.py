# -*- coding: utf-8 -*-
import gl
import collections
#import os
Anlyoutmap = collections.OrderedDict()  

起始day = 0
涨停day = 0
最高day = 0
缩量day = 0
结束day = 0
最高值 = 0
涨停值 = 0
放量均值 = 0
缩量均值 = 0

缩量比例 = 0.6
rulen = 'rule81'

'''
#大中小斜口鸭头
(1)取最高点，高点时和涨停时4线多头排列，最高值
(2)往前10天找涨停，最低值
(3)涨停后5天找放量均值
(4)判断箱体，找缩量均值
#大鸭头：（范围为30天）最高点前10天有涨停，(取第一个涨停)，涨停后5天均量，再20天内有缩量（非跌停）（涨停价和最高价之间）
       （20-25天考虑级差斜率K线）
#小鸭头：（范围为20天）最高点前5天有涨停，取5天均量，再10天内有缩量
'''
def find_rule_81(d, Anlyinmap):
    global Anlyoutmap
    global 起始day,涨停day,最高day,结束day,缩量day,放量均值,缩量均值,缩量比例

    起始day = d - 29
    结束day = d
    '''(1)前10天中找最高点：-29~-20''' 
    最高值 = 0
    for i in range(起始day, 起始day+10):
        if Anlyinmap[i]['基K'][1] > 最高值:
            最高值 =  Anlyinmap[i]['基K'][1]
            最高day = i
        #endof 'if'
    #endof 'for'
    '''涨停时多头排列？？？？？？？？？？？？'''
    #print('1:')
    
    '''(2)起始day~最高day有涨停（第一个涨停，左边开始找）''' 
    for i in range(起始day,最高day+1):
        f_zt = 0
        if Anlyinmap[i]['基K'][3] >= round(1.1 * Anlyinmap[i-1]['基K'][3], 2):
            涨停值 =  Anlyinmap[i]['基K'][3]
            涨停day = i
            f_zt = 1
            break
        #endof 'if'
    #endof 'for'
    if f_zt == 0:   return 0    #无涨停
    '''涨停时多头排列？？？？？？？？？？？？'''
    #print('2:')
    
    '''(3)最高day - 涨停day >= 3天（大鸭头特征）'''#1天（小鸭头特征）
    #if 最高day - 涨停day < 3:   return 0
    if 最高day - 涨停day < 1:   return 0
    #print('3:')
    
    '''(4)涨停day+1 ~ +6：求不超过5天的放量均值'''
    sum_v = 0.0
    j = 0
    for i in range(涨停day+1, min(涨停day+6,最高day+1)):
        #一字涨停量小，剔除
        #if not (Anlyinmap[i]['基K'][0] == Anlyinmap[i]['基K'][1]): #开！=高
        sum_v = sum_v + Anlyinmap[i]['V'][0]
        j = j + 1
        #endof 'if'
    #endof 'for'
    放量均值 = sum_v / j
    #print('4:')
    
    '''(5)最高day+1 ~ 最高day+21(结束day+1)：20天内找缩量均值(2天平均)（非涨跌停）'''
    f_sl = 0
    for i in range(最高day+1,min(结束day,最高day+20)):
        缩量均值 = 0.5 * (Anlyinmap[i]['V'][0] + Anlyinmap[i+1]['V'][0])
        if 缩量均值 > 放量均值*1.5: #？？？？？？？？？？？？？？？？？？？？？？？？？
            f_sl = 0
            break
        elif 缩量均值 < 放量均值*缩量比例:
            if Anlyinmap[i]['基K'][3] < round(1.1*Anlyinmap[i-1]['基K'][3],2) and \
            Anlyinmap[i]['基K'][3] > round(0.9*Anlyinmap[i-1]['基K'][3],2) and \
            Anlyinmap[i+1]['基K'][3] < round(1.1*Anlyinmap[i]['基K'][3],2) and \
            Anlyinmap[i+1]['基K'][3] > round(0.9*Anlyinmap[i]['基K'][3],2) :
                f_sl = 1
                缩量day = i+1
            #endof 'if'
        #endof 'if'
    #endof 'for'   
  
    if f_sl == 0:   return 0 #无缩量/超最大量  
    #print('5:')
    
    '''(6)涨停day+1~缩量day+1：close(low)\high值在箱体中'''#(low)
    f_return = 0  
    for i in range(涨停day+1,缩量day+1):
        if Anlyinmap[i]['基K'][3] < 涨停值*0.99 or Anlyinmap[i]['基K'][1] > 最高值:
            f_return = 1
            break
    #endof 'if'
    #endof 'for'
    if f_return == 1:   return 0 #超出箱体        
    #print('6:')  
    #print(起始day,涨停day,最高day,结束day,缩量day,放量均值,缩量均值)
    
    '''无返回0，则成功'''
    return 1
#endof 'def'       
    

def rule_81(code, Anlyinmap):
    global rulen, Anlyoutmap, 缩量day
    
    cnt = 0
    Anlyoutmap.clear()
        
    #遍历
    for (d,x) in Anlyinmap.items():
        if d < 30:
            continue
        else:
            if 1 == find_rule_81(d, Anlyinmap):
                '''输出'''
                Anlyoutmap[Anlyinmap[缩量day]['date']] = [rulen, '大中小斜口鸭头']
                for i in range(1,3):
                    Anlyoutmap[Anlyinmap[缩量day-i]['date']] = ['rule0', '++']
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
