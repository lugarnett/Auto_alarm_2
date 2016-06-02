# -*- coding: utf-8 -*-
import gl
import os
import tushare as ts
import collections

#模块内全局变量
CodeMap = collections.OrderedDict()

'''通过tushare接口获取数据'''
def mdl_codeget_net():
    global CodeMap
    CodeMap.clear()
    
    #获取code，出错则重试10次
    #for i in range(10):
    try:
        dataframe = ts.get_today_all()  
    except Exception as e:
        print(e)
        print('code获取失败！')
        #continue
    #endof 'try'
        #break
    #endof 'for'
    if dataframe is None:
        return -1, None

    #获取code列表
    #dataframe.sort(['code'], inplace=True)
    n = 0
    for each in dataframe.index:
        code = dataframe.values[n][0]
        name = dataframe.values[n][1]
        CodeMap[n] = [code,name]
        n = n + 1
    #endof 'for' 
    #存入文本
    head = "序号\tcode\tname\n"
    with open(gl.path_data_origin + "A_code.txt", 'w') as out:
        out.write(head)
        for (d,x) in CodeMap.items():
            tmpstr = '%d'%(d+1) + "\t" + "\t".join(str(i) for i in x) + "\n"
            out.write(tmpstr)
        #end of "for"
    #end of "with"
    print('\n\nnet_code获取完成 -> 共%d'%len(CodeMap))
    #print(CodeMap)
    return 1, CodeMap
#endof 'mdl'

'''通过file接口获取数据'''
def mdl_codeget_file(pos):
    global CodeMap
    CodeMap.clear()
    
    if os.path.exists(gl.path_data_origin + "A_code.txt") <= 0:
        return -1, None

    with open(gl.path_data_origin + "A_code.txt", 'r') as f:
        f.readline()
        for i in range(pos-1):
            #print('空读')
            f.readline()
        #end of "for"
        n = pos
        for line in f.readlines():
            strlist = line.split('\t')  # 用tab分割字符串，并保存到列表
            code = strlist[1]
            name = strlist[2]
            CodeMap[n] = [code,name]
            n = n + 1                                
        #end of "for"
    #end of "with"
    print('\n\nfile_code获取完成 -> 共%d'%len(CodeMap))
    return 1, CodeMap
#endof 'mdl'






