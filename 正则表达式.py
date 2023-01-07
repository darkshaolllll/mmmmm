import re
 
 
content = 'Hello 123456789 Word_This is just a test 666 Test'
result = re.match('^Hello\s(\d+).*?Test', content)  # 注意(\d+) 有括号，+号表示匹配一次或多次
# \d数字 \s任意空白字符 {}匹配n个前面的字符
print(result)
print(result.group())    # print(result.group(0)) 同样效果
print(result.groups())#必须得匹配到才行 否则就会出现AttributeError: 'NoneType' object has no attribute 'group'错误
 
print(result.span()) #表示匹配的范围
print(result.group(1))
content = 'hello 1234567 world_this is a regex demo'
result = re.match('^hello\s(\d+)\sworld',content)
print(result)
print(result.group())
print(result.span())
result1=re.match('^hello\s(\d+)\sword',content)
print(result1.group(1))#匹配第一个被()包裹的结果