from urllib import response
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

from zmq import proxy
proxy_handler=ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'http://127.0.0.1:9743'#端口可能还没有搭建
})#使用相关的 Handler处理器 来创建特定功能的处理器对象
opener=build_opener(proxy_handler)#然后通过 build_opener()方法使用这些处理器对象，创建自定义opener对象
try:
    response=opener.open('https://www.baidu.com')#使用自定义的opener对象，调用open()方法发送请求。
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)