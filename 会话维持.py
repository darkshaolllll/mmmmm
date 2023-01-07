import requests
requests.get('http://httpbin.org/cookies/set/number/123456789')
r=requests.get('http://httpbin.org/cookies')#相当于打开了两个浏览器cookie是不同的
print(r.text)
s=requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r=s.get('http://httpbin.org/cookies')#相当于同一个浏览器打开了两个标签
print(r.text)
#现在还不明白一些底层的内容