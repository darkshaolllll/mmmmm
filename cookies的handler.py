from cgitb import handler
from fileinput import filename
import http.cookiejar,urllib.request
from tokenize import cookie_re
from urllib import response
filename='cookies.txt'
#cookie=http.cookiejar.CookieJar()#先声明http.cookiejar模块并获取一种取得cookie的方法
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)#构建一个handler
opener=urllib.request.build_opener(handler)#利用handler构建出一种特殊的open执行函数
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
#for item in cookie:
#    print(item.name+"="+item.value)
#很多的内容还是不清楚