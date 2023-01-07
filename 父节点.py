from lxml import etree

html=etree.parse('./testxpath.html',etree.HTMLParser())
result=html.xpath('//a[@href=""]/parent::*/@class')#@是属性匹配
print(result)