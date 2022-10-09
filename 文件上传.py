import requests
files={'file':open('favicon.ico','rb')}
r=requests.post("http://httpbin.org/post",files=files)#表单为空 文件上传会有一个单独的部分进行标识
print(r.text)