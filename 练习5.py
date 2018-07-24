# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:14:57 2018

@author: samsung
"""

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

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
