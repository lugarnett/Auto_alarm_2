# -*- coding: gbk -*-
import datetime

#ϵͳȫ�ֱ�������
STCode = '600000'
STName = ''

todaydate = datetime.datetime.now().strftime("%Y-%m-%d")

path_data_origin = 'ԭʼ����\\ԭʼ����' + todaydate + '\\'
path_data_avg = '��ֵ��������\\��ֵ��������' + todaydate + '\\'
path_rule_rst = '����������\\����������' + todaydate + '\\'
path_view_rst = 'ͼƬ���\\ͼƬ���' + todaydate + '\\'
path_email_rst = '�ʼ���¼\\'

Fig_Cnt = 1

��Ϣdict = {'����̬��Ҫ': [], '����̬һ��': [], '������̬��Ҫ': [], '������̬һ��': [], '��̬3��һ��': []}

'''ruleAnly����������'''
##���ݿ��ж�ȡ���ݷ�������������ͼʱK��ʱ��������Ҫ��֤>=��rule��������
Analyse_days_date = 60
Anly_days_add = 3    #����n��ķ���
#rules����С��������
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

Anly_days_121 = 2    ####1��������ͣ��������Anly_days_add

'''whlAnly����������'''
whlAnly_1 = 5         ####������Anly_days_add
'''whlAnly��ر�����ʼ��'''
������ͣ�� = 0
����ѡ����= 0
ZT_1����5�� = 0
ZT_1����5��N = 0
ZT_1����5���� = 0.0
ZT_2����5�� = 0
ZT_2����5��N = 0
ZT_2����5���� = 0.0
ZT_1�����2����5�� = 0
ZT_1�����2����5��N = 0
ZT_1�����2����5���� = 0.0
ZT_1�����3����5�� = 0
ZT_1�����3����5��N = 0
ZT_1�����3����5���� = 0.0
XG_1����5�� = 0
XG_1����5��N = 0
XG_1����5���� = 0.0
XG_2����5�� = 0
XG_2����5��N = 0
XG_2����5���� = 0.0
####����ɸѡ��ǰ���������
Date0 = ''
Cnt_0 = 1