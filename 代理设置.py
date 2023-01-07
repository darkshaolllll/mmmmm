import requests
proxies={
    "http":"http://user:password@10.10.1.10:3128",
}
requests.get("https://www.taobao.com",proxies=proxies)
r=requests.get("https://www.taobao.com",timeout=(5,11,30))#连接读取与总和可以设定为none或直接空着为永久
print(r.status_code)