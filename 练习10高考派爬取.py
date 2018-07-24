# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:22:10 2018

@author: Administrator
"""
#####高校招生人数（河南）
ls=open('all_school.txt',encoding='utf-8').readlines()
schoolls=[]
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}
for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
f=open('河南数据2.txt','a',encoding='utf-8')
for schoolid in schoolls[0:2300]:
    for kemu in [1,2]:
        req=r.Request(url,data='id={}&type={}&city=41&state=1'.format(schoolid,kemu).encode(),headers=headers)
        f.write(r.urlopen(req).read().decode('utf-8','ignore')+"\n")
f.close()





##1.2300所学校的编号
file=open('all_school.txt',encoding='utf-8').readlines()
print('2300所学校的编号：\n')
for i in range(len(file)):
    print(file[i].split('-jianjie-')[1].split('.')[0])


##2.31所城市的编号
file2=open('XML高考派城市.txt',encoding='gbk').readlines()
print('31所城市的编号：\n')
for k in range(1,32):
    print(file2[k].split('<li data-val=')[1].split('data-id=')[0]+file2[k].split('claimCity')[1].split(',')[1].split(')')[0])

    
    
    
    
    
    