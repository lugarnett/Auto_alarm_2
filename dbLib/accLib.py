# -*- coding: utf-8 -*-
import gl
import os
import tushare as ts
import collections
import json
import win32com.client

#-------------access数据模块--------------

class Access_Model:

    def __init__(self,dataUrl):
        self.dataUrl =dataUrl
###定义conn
    def db_conn(self):
        conn = win32com.client.Dispatch(r'ADODB.Connection')
        dns = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE='+self.dataUrl
        conn.Open(dns)
        return conn
####定义rs
    def db_rs(self):
        rs = win32com.client.Dispatch(r'ADODB.Recordset')
        rs.CursorType = 1;
        rs.CursorLocation = 3 # don't use parenthesis here
        rs.LockType = 3;#可读可写模式
        return rs
####关闭数据库
    def db_close(self):
        conn=self.db_conn()
        conn.Close()
####获取数据库所有记录集
    def db_query(self,sql):
        conn=self.db_conn()
        rs=self.db_rs()
        rs.Open(sql,conn)
        #print (rs.RecordCount)
        dataStr = ""
        arrData =[]
        rs.MoveFirst()
        while (rs.EOF==False and rs.BOF==False):
            i= 0

            dataStr ="{"
            while i<rs.Fields.Count:
                dataStr +="\""+rs.Fields(i).name+"\""+":"+"\""+str(rs.Fields(i).value)+"\""
                if(i<rs.Fields.Count-1):
                    dataStr +=","
                i=i+1
            dataStr +="}"
            arrData.append(dataStr)#JSON数据
            rs.MoveNext()
        rs.Close()
        self.db_close()
        return arrData
####增加记录
    def db_add(self,sql):
        # sql="insert into addresslist(name,department,cellphone) values('name','department','13xxxxxxxxxx')";
        try:
            conn=self.db_conn()
            conn.execute(sql);
            conn.Close()
            return True
        except (TypeError,ValueError) as e:
            conn.Close()
            return False  
####修改记录
    def db_modi(self,sql):
        #sql="update addresslist set name='name' where id=2"
        try:
            conn=self.db_conn()
            conn.execute(sql);
            conn.Close()
            return True
        except (TypeError,ValueError) as e:
            conn.Close()
            return False  
####删除记录
    def db_del(self,sql):
         #sql="delete * from addresslist where id=2"
        try:
            conn=self.db_conn()
            conn.execute(sql);
            conn.Close()
            return True
        except (TypeError,ValueError) as e:
            conn.Close()
            return False 
         
####获取数据库记录总数
    def db_recordcount(self,sql):
        conn=self.db_conn()
        rs=self.db_rs()
        rs.Open(sql,conn)
        #print (rs.RecordCount)
        count =0
        if(rs.EOF==False and rs.BOF==False):
            count= rs.RecordCount

        rs.Close()
        self.db_close()
        return  count      
        
####示例
def mdl_db_Forexample():
    try:
        dataUrl =os.getcwd()+"\\opp.accdb"
        data = Access_Model(dataUrl)
    
        sql ="Select * FROM addresslist order by id asc" 
        dataRecordSet =data.db_query(sql)
        print(data.db_recordcount(sql))
        #print(len(dataRecordSet))
        for item in dataRecordSet:
            a =eval("("+item+")")#eval解析JSON数据
            print (a['department'])#department为字段名
        ###
            
        sql="update addresslist set name='name' where id=2";
        if(data.db_modi(sql)):
            print("修改完成！")
        else:
            print("修改失败")

        sql="delete * from addresslist where id=2"
        if(data.db_modi(sql)):
           print("删除成功！")
        else:
            print("删除失败")
    except (TypeError,ValueError) as e: #将异常对象输出
        print("error:"+str(e))





