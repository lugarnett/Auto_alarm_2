## 计算4条均线

import gl

import collections

#模块内全局变量
datamap = collections.OrderedDict()

def Avg_proc(code):
    global datamap

    day = len(datamap)
    if day <= 60:
        return
        
    #增加换手数据
    for key in datamap:
        datamap[key].extend([0.0])
        
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
    #endof "for"
            
    head2 = "时间\t开盘\t最高\t最低\t收盘\t总手\t金额\t换手%\tavg5\tavg10\tavg20\tavg30\tavg60\n"
    with open(gl.path_data_avg + code + "_avg.txt", 'w') as out:
        out.write(head2)
        for key in datamap:
            if key >= 60:
                tmpstr = "\t".join(str(i) for i in datamap[key]) + "\n"
                out.write(tmpstr)
        #endof "for"
    #endof "with"
#endof "Avg_proc()"


def mdl_calcAvrg(DatasrcMap):
    global datamap

    datamap = DatasrcMap   
    code = gl.STCode
    Avg_proc(code)
    print("2:均值处理完毕！")
    datamap.clear()
#endof 'def'
