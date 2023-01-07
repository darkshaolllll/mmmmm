import re
content = '''hello 1234567 world_this
is a regex demo'''
result =re.match('^he.*?(\d+).*?demo$',content,re.S)#re.s 转义字符使.能够匹配换行符
print(result.group(1))
content= '(百度)www.baidu.com'
result=re.match('\(百度\)www\.baidu\.com',content)
print(result.group())
