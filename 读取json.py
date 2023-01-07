import json
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''#数组用[] 对象用键值对{}
print(type(str))
data=json.loads(str)
print(data)
print(type(data))
with open('pp.json','w',encoding='utf-8') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))#可以存在中文
date=json.load(open('7号房的礼物 - 7번방의 선물.json',encoding='utf-8'))
print(date)