# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:48:58 2018
1.加载网络数据(现在不是重点，要会记住，可以复制)
2.解析字典数据(重点分析)
练习题3：
1.通过复制联网天气代码，获取老家的天气字典
2.打印温度temp,天气情况description 天气气压pressure
@author: Administrator
"""

#练习三

city=input('Please enter the name of you want to inquire.')
import urllib.request as n
data=n.urlopen('http://api.openweathermap.org/data/2.5/weather?q={},cn&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')

import json
data=json.loads(data)

###data字典---》main字典-》temp变量
###data字典---》wind字典--》speed变量

print ('气温：'+str(data['main']['temp']))
print ('情况：'+str(data['weather'][0]['description']))   ###weather为列表
print ('气压'+str(data['main']['pressure']))
