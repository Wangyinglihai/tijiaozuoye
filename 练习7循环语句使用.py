# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 19:28:39 2018
练习7
1、使用多选其一，完成天气的提醒，淘宝客户端
2、一定要多次使用for循环，偶尔使用while循环，在淘宝客户端
3、使用到break或者continue，在淘宝客户端
@author: Administrator
"""
#练习7.1
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

def day(a,b):
    print('第'+str(a)+'天：')
    print('temper:'+str(data['list'][b]['main']['temp']))
    print('description：'+str(data['list'][b]['weather'][0]['main']))
    x=str(data['list'][b]['weather'][0]['main'])
    if x=='Clouds':
        print('温馨提示：多云,冷热适宜，较舒适')
    elif x=='Clear':
        print('温馨提示：天气晴朗，宜出行')
    elif x=='Rain':
        print('温馨提示：有雨，出门带伞')
    print('#'*20)
day(1,2)
day(2,10)
day(3,18)
day(4,26)
day(5,34)



url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

for n in range(0,36):
    print('商品'+str(n+1))
    print('名称：'+str(data['mods']['itemlist']['data']['auctions'][n]['raw_title']))
    print('价格：'+str(data['mods']['itemlist']['data']['auctions'][n]['view_price']))
    print('地点：'+str(data['mods']['itemlist']['data']['auctions'][n]['item_loc']))
    print('销量：'+str(data['mods']['itemlist']['data']['auctions'][n]['view_sales']))
    a=str(data['mods']['itemlist']['data']['auctions'][n]['view_sales'])
    b=int(a[0:-3])
    if b>10000:
        print('****温馨提示：销量报表，非常受欢迎，快去抢购')
    elif b>100:
        print('****温馨提示：销售情况较好，放心选购')
    else:
        print('****销量较少，请谨慎购买')
        
#7.2
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

for i in range(0,36):
        a=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        print('第'+str(i+1)+'件商品的价格为：'+str(a)+'元')
        while int(a)>200:
            print('----------------------------该商品价格高于200元')
            break
        if (i+1)%4==0:
              print('*'*40) 
#7.3
print('销量大于10000的商品为：')
def sales():
    for i in range(0,36):
        a=str(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
        b=int(a[0:-3])
        if i==20:
            break
        if b<10000:
            continue
        print('第'+str(i+1)+'件：'+str(b))
sales()
        
