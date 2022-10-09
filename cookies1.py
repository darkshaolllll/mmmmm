from http import cookies
from multiprocessing.sharedctypes import Value
import requests
r=requests.get("https://www.baidu.com")#该方法获得是requestcookiejar类型用items()方法将其转化为由元组组成的列表
print(r.cookies)
for key,value in r.cookies.items():
    print(key+'='+value)#将其遍历