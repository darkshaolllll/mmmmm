import requests 
import re
from pyquery import PyQuery as pq
url='https://ssrl.scrape.center/'
html=requests.get(url).text
doc=pq(html)
items=doc('.el-card').items()
file=open('movies.txt','w',encoding='utf-8')
for item in items:
    name=item.find('a>h2').text()
    file.write(f'名称{name}\n')
file.close()