# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:20:01 2018

练习题8：保存淘宝数据（小组项目）
1.每个组员爬取某个商品100页数据 每个组员爬取的城市不同 上海，北京，成都
2.保存淘宝商品信息，并且保存为txt文件
3.每组组长合并各组员的数据

@author: Administrator
"""
try:
    def p(n):
        import urllib.request as r#导入联网工具包，名为为r
        page=n*44
        url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E5%90%89%E6%9E%97&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'
        data=r.urlopen(url.format(page)).read().decode('utf-8','ignore')

        import json#将字符串转换为字典
        data=json.loads(data)
        a=json.dumps(data)
        f=open('裙子吉林2.txt','a',encoding='utf-8')
        f.write(a+'\n')
        f.close()
    for n in range(0,100):
        p(n)
        print(n)
except Exception as err:
    print('发生错误了')

