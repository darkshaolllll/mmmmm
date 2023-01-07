from importlib.resources import contents
from multiprocessing import context
from urllib import response
import urllib.request
url_page='http://www.baidu.com'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
request=urllib.request.Request(url=url_page,headers=headers)
response=urllib.request.urlretrieve(request)
content=response.read().decode('utf-8')
print(content)
