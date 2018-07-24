# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:00:03 2018
1、显示4个商品然后打印分割线，只要第一页36个商品信息
2、列出36个商品
3、获取所有的商品价格并且给商品排序，从高到低排序
4、按照销量排序
5、商品过滤，只要15天退款或包邮的商品信息，显示
@author: Administrator
"""

#6.1
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

def goods():
    for n in range(0,36):
        print('商品'+str(n+1))
        print('名称：'+str(data['mods']['itemlist']['data']['auctions'][n]['raw_title']))
        print('价格：'+str(data['mods']['itemlist']['data']['auctions'][n]['view_price']))
        print('地点：'+str(data['mods']['itemlist']['data']['auctions'][n]['item_loc']))
        print('销量：'+str(data['mods']['itemlist']['data']['auctions'][n]['view_sales']))
        if((n+1)%4==0):
            print('*'*80)
goods()

#6.2  商品列表
for n in range(0,36):
    print('商品{}:'.format(str(n+1))+str(data['mods']['itemlist']['data']['auctions'][n]['raw_title']))

#6.3 价格排序
def price(i):
    z=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    return z
a=[price(0),price(1),price(2),price(3),price(4),price(5),price(6),price(7),price(8),price(9),
   price(10),price(11),price(12),price(13),price(14),price(15),price(16),price(17),price(18),
   price(19),price(20),price(21),price(22),price(23),price(24),price(25),price(26),price(27),
   price(28),price(29),price(30),price(31),price(32),price(33),price(34),price(35)]
print('价格从高到低的排序为：')
b=sorted(a)
c=list(reversed(b))
print(c)

#6.4销量排序
def s(i):
    z=str(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    m=int(z[0:-3])
    return m
x=[s(0),s(1),s(2),s(3),s(4),s(5),s(6),s(7),s(8),s(9),s(10),s(11),s(12),s(13),s(14),s(15),
    s(16),s(17),s(18),s(19),s(20),s(21),s(22),s(23),s(24),s(25),s(26),s(27),s(28),s(29),
    s(30),s(31),s(32),s(33),s(34),s(35)]
print('销量的排序为：')
print(sorted(x))

#######
s=[]
def sal():
    for i in range(0,36):
        z=str(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
        m=int(z[0:-3])
        s.append(m)   ###追加列表元素
    return s
sal()
print('销量的排序为：')
print(sorted(s))

#6.5包邮商品
for i in range(0,36):
    if float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.0:
        print('第{}件商品包邮'.format(str(i+1))+str(data['mods']['itemlist']['data']['auctions'][i]['raw_title']))


#####################
def free():
    for i in range(0,36):
        n=['15天退货']#######15天退货，有错误
        m=str(data['mods']['itemlist']['data']['auctions'][i]['icon'][2]['iconPopupComplex'][1]['subIcons'][0]['icon_content'])
        p=['m']
        for n in p:
            print('第'+str(i+1)+'件商品15天退货:'+str(data['mods']['itemlist']['data']['auctions'][i]['raw_title']))
        if float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.0:
            print('第'+str(i+1)+'件商品包邮:'+str(data['mods']['itemlist']['data']['auctions'][i]['raw_title']))
free()



