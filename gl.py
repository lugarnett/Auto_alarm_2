# -*- coding: gbk -*-
import datetime

#系统全局变量定义
STCode = '600000'
STName = ''

todaydate = datetime.datetime.now().strftime("%Y-%m-%d")

path_data_origin = '原始数据' + todaydate + '\\'
path_data_avg = '均值整理数据' + todaydate + '\\'
path_rule_rst = '规则分析结果' + todaydate + '\\'
path_view_rst = '图片结果' + todaydate + '\\'

Fig_Cnt = 1

##数据库中读取数据分析的天数，画图时K线时间天数
Analyse_days_date = 60
Anly_days_add = 15    #增加n天的分析
#rules的最小分析天数
Anly_days_1 = 2
Anly_days_2 = 2
Anly_days_3 = 2
Anly_days_4 = 2
Anly_days_5 = 1
Anly_days_6 = 1
Anly_days_7 = 3
Anly_days_8 = 3
Anly_days_9 = 3
Anly_days_10 = 2
Anly_days_11 = 5
Anly_days_12 = 2
Anly_days_13 = 2
Anly_days_14 = 3
Anly_days_15 = 3
Anly_days_16 = 2
Anly_days_17 = 2
Anly_days_18 = 2
Anly_days_19 = 1

Anly_days_50 = 6
Anly_days_51 = 7
Anly_days_52 = 16
Anly_days_53 = 21

Anly_days_80 = 36
Anly_days_81 = 32
#Anly_days_82 = 6-30

'''不包含Anly_days_add'''
Anly_days_121 = 10



