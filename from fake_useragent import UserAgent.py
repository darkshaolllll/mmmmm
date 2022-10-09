from urllib import parse
url='http://www.baidu.com/s?wd={}'
word=input('请输入要输入的内容:')
query_string=parse.quote(word)
print(url.format(query_string))