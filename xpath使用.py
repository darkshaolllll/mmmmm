from lxml import etree
html=etree.parse('./testxpath.html',etree.HTMLParser())
result=html.xpath('//ul/a')#ul下没有直接的a节点
print(result)#返回的是一个列表
print(result[0])#返回列表的第一个元素