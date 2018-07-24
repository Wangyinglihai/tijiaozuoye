# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:14:57 2018
练习题5：
1.优化代码  用函数的方式修改作业4  输出每一天的天气（函数）
2.打印温度折线图，使用函数优化（有返回值）
@author: samsung
"""

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
def weather(a,b):
    print('this day is'+str(a)+'天的天气情况')
    print('情况：'+str(data['list'][b]['weather'][0]['main']))
weather(2,1)
weather(10,2)
weather(18,3)
weather(26,4)
weather(34,5)



def p(a):
    data1=data['list'][a]['main']['temp']
    num=str('-')*int(data1)
    return num
print('day1'+p(1))
print('day2'+p(2))
print('day3'+p(3))
print('day4'+p(4))
print('day5'+p(5))

