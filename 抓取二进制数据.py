import requests
r=requests.get("https://github.com/favicon.ico")#text 是字符串类型 content 是二进制类型
with open('favicon.ico','wb') as f:#with 可以自动被关闭文件f.close() wb指打开一个文件用于读写如果该文件已存在则覆盖，如果不存在则创建一个新的 f 指代为f
    f.write(r.content) #将r.content里面的内容写入到f里面