# -*- coding: utf-8 -*-
import gl
import tushare as ts
import collections

#模块内全局变量
CodeMap = collections.OrderedDict()

'''通过tushare接口获取数据'''
def mdl_codeget():
    global CodeMap
    CodeMap.clear()
    
    #获取code，出错则重试10次
    for i in range(10):
        try:
            dataframe = ts.get_today_all()  
        except Exception as e:
            print('\n'+e)
            print('code获取失败！')
            continue
        #endof 'try'
        break
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
    with open(gl.path_data_origin + "_code.txt", 'w') as out:
        out.write(head)
        for (d,x) in CodeMap.items():
            tmpstr = '%d'%(d+1) + "\t" + "\t".join(str(i) for i in x) + "\n"
            out.write(tmpstr)
        #end of "for"
    #end of "with"
    print('\n\ncode获取完成！')
    print(CodeMap)
    return 1, CodeMap
#endof 'mdl'










