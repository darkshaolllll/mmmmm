from urllib.parse import urlencode
params={
    'name':'germey',
    'age':22
}#反序列化转为字典型（qs）或由元组组成的列表(qsl'<LO)))，序列化转为get请求参数
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)