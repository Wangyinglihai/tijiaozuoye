# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:44:59 2018
练习题4：
1.打印每天18点的天气信息，温度，情况，气压，最高温度，最低温度
2.写出英文版的天气-天气情况，用户输入英文   application应用
3.打印温度折线图
    1----------
    2--------------------
    3-------
    4----------
4.获取所有的温度，并且排序（sorted([1,4,-1,8])##########使用此方法排序）
5.友情提示，根据温度提示穿衣，打伞，出门(可选)

全球5天天气
@author: Administrator
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

#####温度，气压
#data字典-》list列表-》0 index字典-》main字典-》temp变量
data['list'][0]['main']['temp']
#data字典-》list列表-》0 index字典-》wind字典-》speed变量
data['list'][0]['wind']['speed']







print('day1')
print('temp'+str(data['list'][2]['main']['temp']))
print('description'+str(data['list'][2]['weather'][0]['description']))
print('pressure'+str(data['list'][2]['main']['pressure']))
print('temp_max'+str(data['list'][2]['main']['temp_max']))
print('temp_min'+str(data['list'][2]['main']['temp_min']))

print('day2')
print('temp'+str(data['list'][10]['main']['temp']))
print('description'+str(data['list'][10]['weather'][0]['description']))
print('pressure'+str(data['list'][10]['main']['pressure']))
print('temp_max'+str(data['list'][10]['main']['temp_max']))
print('temp_min'+str(data['list'][10]['main']['temp_min']))

print('day3')
print('temp'+str(data['list'][18]['main']['temp']))
print('description'+str(data['list'][18]['weather'][0]['description']))
print('pressure'+str(data['list'][18]['main']['pressure']))
print('temp_max'+str(data['list'][18]['main']['temp_max']))
print('temp_min'+str(data['list'][18]['main']['temp_min']))

print('day4')
print('temp'+str(data['list'][26]['main']['temp']))
print('description'+str(data['list'][26]['weather'][0]['description']))
print('pressure'+str(data['list'][26]['main']['pressure']))
print('temp_max'+str(data['list'][26]['main']['temp_max']))
print('temp_min'+str(data['list'][26]['main']['temp_min']))

print('day5')
print('temp'+str(data['list'][34]['main']['temp']))
print('description'+str(data['list'][34]['weather'][0]['description']))
print('pressure'+str(data['list'][34]['main']['pressure']))
print('temp_max'+str(data['list'][34]['main']['temp_max']))
print('temp_min'+str(data['list'][34]['main']['temp_min']))


temper=[data['list'][2]['main']['temp'],
data['list'][10]['main']['temp'],
data['list'][18]['main']['temp'],
data['list'][26]['main']['temp'],
data['list'][34]['main']['temp']]
print('the sorted tempreture is:')

a='-'*(data['list'][2]['main']['temp'])
b='-'*(data['list'][10]['main']['temp'])
c='-'*(data['list'][18]['main']['temp'])
d='-'*(data['list'][26]['main']['temp'])
e='-'*(data['list'][34]['main']['temp'])

print('The line chart is:')
print(a)
print(b)
print(c)
print(d)
print(e)

city=input('please enter  the name of city')
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url.format(city)).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

  



    
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

print('')
def pl(s):
    return(int(data['list'][s]['main']['temp']))
print(sorted([pl(2),pl(10),pl(18),pl(26),pl(34)]))








url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
print('the sorted tempreture is:')
temper=[data['list'][2]['main']['temp'],
data['list'][10]['main']['temp'],
data['list'][18]['main']['temp'],
data['list'][26]['main']['temp'],
data['list'][34]['main']['temp']]

print(sorted(temper))

print('温度折线图')
print('day1:'+'-'*int(data['list'][2]['main']['temp']))
print('day2:'+'-'*int(data['list'][10]['main']['temp']))
print('day3:'+'-'*int(data['list'][18]['main']['temp']))
print('day4:'+'-'*int(data['list'][26]['main']['temp']))
print('day5:'+'-'*int(data['list'][34]['main']['temp']))