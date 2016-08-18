#coding: utf-8
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText

def snd_email(信息dict):
    发送地址 = '214194800@qq.com'
    授权码 = 'qiawkvnkxyrzbhja'
    收信列表 = ['214194800@qq.com']
    subject = time.strftime("%Y%m%d_%H:%M",time.localtime(time.time()))
    
    '删除重复code'
    for code in 信息dict['一般']:
        if code in 信息dict['重要']:
            pos = 信息dict['一般'].index(code)
            信息dict['一般'].pop(pos)
    #end for 
    
    邮件内容 = ""
    for (d,x) in 信息dict.items():
        邮件内容 += d + ':\n'
        邮件内容 += ',\t'.join(x) + '\n\n'
    #end for
    msg = MIMEText(邮件内容)
    msg['From'] = Header('gzz')
    msg['Subject'] = Header(subject)

    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.starttls()
        server.login(发送地址, 授权码)
        snd_status = server.sendmail(发送地址, 收信列表, msg.as_string())
        if snd_status == {}:      
            print("邮件发送成功！"  ) 
        else:      
            print ("邮件发送失败。。。" )
    except Exception as e:      
        print(e)      
    server.quit()
#end def

信息dict = {'重要': ['666','111'], '一般': ['666','000']}
snd_email(信息dict)

