# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:28:24 2021

@author: Administrator
"""

dic = {}
n = int(input())
for i in range(n):
    req = str(input())
    if req not in dic.keys():
        print('OK')
        dic[req] = 1
    else:
        print(req + str(dic.get(req)))
        dic[req]+=1
