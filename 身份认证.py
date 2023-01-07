import requests
from requests.auth import HTTPBasicAuth
r=requests.get('http://localhost:5000',auth=('username','password'))#auth为一个元组默认使用HTTPBasicAuth验证
print(r.status_code)