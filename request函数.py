from urllib import parse,request, response
#request=urllib.request.Request('https://python.org')#将请求变化成一个对象使之更以调控
#response=urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))
url='http://httpbin.org/post'#请求的链接
headers={
    'User-Agent':'User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Host':'httpbin.org'
}#请求头
dict={
    'name':'Germey'
}#上传的数据
data=bytes(parse.urlencode(dict),encoding='utf-8')
req=request.Request(url=url,data=data,headers=headers,method='POST')
response=request.urlopen(req)
print(response.read().decode('utf-8'))