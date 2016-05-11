## 计算4条均线


import glbVar

import os
import collections

'''
def Avg_proc(file):

    datamap.clear()
    day = 0

    with open(path_data_origin + file, 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # 用tab分割字符串，并保存到列表
            n = 0
            for value in strlist:
                if not value:
                    strlist.pop(n)
                n = n + 1
            #end of "for"
            if len(strlist) < 9:
                continue
            else:
                datamap[day] = [strlist[0].replace('-',''), float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4]), int(strlist[7].replace(',','')), int(strlist[8].replace(',','')), float(strlist[9])]
                day = day + 1
        #end of "for"
    #end of "with"

        
    for key in datamap:
        if key >= 60 and key < day:
            avg5 = 0
            avg10 = 0
            avg20 = 0
            avg30 = 0
            avg60 = 0
            for x in range(key-4, key+1):
                avg5 = avg5 + datamap[x][4]/5
            for x in range(key-9, key+1):
                avg10 = avg10 + datamap[x][4]/10
            for x in range(key-19, key+1):
                avg20 = avg20 + datamap[x][4]/20
            for x in range(key-29, key+1):
                avg30 = avg30 + datamap[x][4]/30
            for x in range(key-59, key+1):
                avg60 = avg60 + datamap[x][4]/60
            #累加得到均线
            datamap[key].extend([float("%.2f"%avg5), float("%.2f"%avg10), float("%.2f"%avg20), float("%.2f"%avg30), float("%.2f"%avg60)])
    #end of "for"
            
    head2 = "时间\t开盘\t最高\t最低\t收盘\t总手\t金额\t换手%\tavg5\tavg10\tavg20\tavg30\tavg60\n"
    with open(path_data_avg + file[:-4]+"_avg.txt",'w') as out:
        out.write(head2)
        for key in datamap:
            if key >= 60:
                tmpstr = "\t".join(str(i) for i in datamap[key]) + "\n"
                out.write(tmpstr)
        #end of "for"
    #end of "with"
#end of "Avg_proc()"
'''

def mdl_calcAvrg():
    #Avg_proc(STCode)
    print(glbVar.STCode)
    print("均值处理完毕！\n")
#endof 'def'
