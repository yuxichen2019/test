# -*- coding: utf-8 -*-
# 2019/11/21 9:59 
# Test
# MD5.py 
# company

#
#
# dict = {"method":"sohan.m2m.iccid.customerBagList","username":"一级客户","timestamp":"1574302713314"}
# a=[]
# for a in dict.keys():
#     a.append(ord(a[0]))
#     if a.count(ord(a[0]))>1:
#

# string=[]
# for x in dict1.items():
#     string.append(x)
#
# print(string)
# for i in string:

import hashlib
import time
import json

millis = str(int(round(time.time() * 1000)))
dic = {
    "username": "一级客户",
    "timestamp": millis,
    "ctime":"",
    "method":"sohan.m2m.iccid.customerBagList"
}
def sign(**dic):
    dict1 = {}
    dict2 = {}
    #过滤值为空的
    for i in dic.keys():
        if dic.get(i) == '' or dic.get(i) == None:
            pass
        else:
            dict1[i] = dic[i]
    #print('dict1:',dict1)
    stringA = ''
    for k in sorted(dict1):
        stringA += (k + '=' + dic[k] + '&')
    #print(stringA)
    stringSignTemp = stringA + 'key=HNlWEvapIcnHIwvWK55lz79j5AKlQQd9'
    #print(stringSignTemp)
    md5 = hashlib.md5()
    md5.update(stringSignTemp.encode(encoding='utf-8'))
    #md5.hexdigest()返回的是十六进制
    sign = md5.hexdigest()
    #转为大写
    signValue = sign.upper()
    dict1['sign'] = signValue
    for p in sorted(dict1):
        dict2[p]=dict1[p]
    print(json.dumps(dict2,ensure_ascii=False).replace(', ',',').replace(': ',':')) #ensure_ascii=False对中文不转化
    #print(json.dumps(dict2,indent=4,ensure_ascii=False))
sign(**dic)