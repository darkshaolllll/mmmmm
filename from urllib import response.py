from urllib import response
import socket
import urllib.request
import urllib.error
#response=urllib.request.urlopen('https://httpbin.org/get',timeout=1)#因为1秒的响应时间很长所以不会报错
try:
    response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.001)#报错类型因为少写了一个/而发生错误
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):#isinstance函数指定一个变量为第一个参数，看是否与第二个参数指定的类型符合
        print('time out')
#print(response.read())