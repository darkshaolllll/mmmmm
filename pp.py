from email import header
from urllib import request
url= 'http://httpbin.org/get'
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'
}
req=request.Request(url=url,headers=headers)
res=request.urlopen(req)
html=res.read().decode('utf-8')
print(html)