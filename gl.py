# -*- coding: gbk -*-
import datetime

#系统全局变量定义
STCode = '600000'
STName = ''

todaydate = datetime.datetime.now().strftime("%Y-%m-%d")

path_data_origin = '原始数据\\原始数据' + todaydate + '\\'
path_data_avg = '均值整理数据\\均值整理数据' + todaydate + '\\'
path_rule_rst = '规则分析结果\\规则分析结果' + todaydate + '\\'
path_view_rst = '图片结果\\图片结果' + todaydate + '\\'
path_email_rst = '邮件记录\\'

Fig_Cnt = 1

信息dict = {'大形态重要': [], '大形态一般': [], '基本形态重要': [], '基本形态一般': [], '形态3个一般': []}

'''ruleAnly的天数设置'''
##数据库中读取数据分析的天数，画图时K线时间天数（要保证>=各rule的天数）
Analyse_days_date = 60
Anly_days_add = 3    #增加n天的分析
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

Anly_days_121 = 2    ####1天内有涨停，不包含Anly_days_add

'''whlAnly的天数设置'''
whlAnly_1 = 5         ####不包含Anly_days_add
'''whlAnly相关变量初始化'''
当天涨停数 = 0
当天选股数= 0
ZT_1天涨5数 = 0
ZT_1天涨5数N = 0
ZT_1天涨5比例 = 0.0
ZT_2天涨5数 = 0
ZT_2天涨5数N = 0
ZT_2天涨5比例 = 0.0
ZT_1天买进2天涨5数 = 0
ZT_1天买进2天涨5数N = 0
ZT_1天买进2天涨5比例 = 0.0
ZT_1天买进3天涨5数 = 0
ZT_1天买进3天涨5数N = 0
ZT_1天买进3天涨5比例 = 0.0
XG_1天涨5数 = 0
XG_1天涨5数N = 0
XG_1天涨5比例 = 0.0
XG_2天涨5数 = 0
XG_2天涨5数N = 0
XG_2天涨5比例 = 0.0
####用于筛选当前处理的日期
Date0 = ''
Cnt_0 = 1