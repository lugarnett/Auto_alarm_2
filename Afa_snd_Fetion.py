import os  
import re  
import sys  
import time    
from pyfetion.fetion import *
#from pyfetion import *
  
def Fetion_Send(msg):  
    account = '18674865324'  # 手机号  
    password = 'lyq20020815'  # 登录密码  
    to_tel = ['13581533894']  # 发送对象飞信号  

    oo = Fetion(account, password)
    loginStatus = oo.login()
    print(loginStatus)
    addStatus = oo.add_friend(to_tel)
    print(addStatus)
    sendStatus = oo.send(to_tel, msg)
    print(sendStatus)
    oo.logout()
#end def
    
def Msg_Snd(msg):
    print ("准备飞信发送。。。"  )
    #注意发送文本长度限制！！！！
    
    Fetion_Send(msg)  
    print ("Done."  )
#end def

msg = "ccc"
Msg_Snd(msg)


