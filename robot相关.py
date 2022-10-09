from urllib.robotparser import RobotFileParser
rp=RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')#设置robot的链接也可是在声明时直接设置
rp.read()#只是执行了读取操作并不会返回任何内容，但如果不写其他函数都会被返回false
#当parse分析整个robot时可起到与read()相同的效果
rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))#判断网页是否可以被抓取