from lxml import etree
html=etree.parse('./testxpath.html',etree.HTMLParser())
result=html.xpath('//li[contains(@class,"li")]//text()')#li的子节点是li
#[contains(@class,"li")]class有两个属性
print(result)
