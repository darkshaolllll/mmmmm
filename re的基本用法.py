import requests
r=requests.get('https://www.baidu.com/')#可以加上一个headers信息
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
data={
    'name':'germey',
    'age':22
}
r=requests.get("http://httpbin.org/get",params=data)
print(r.text)#返回字符串类型
print(r.json())#返回字典