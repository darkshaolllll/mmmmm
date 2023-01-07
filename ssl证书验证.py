from urllib import response
import requests
import logging
response=requests.get('https://www.12306.cn',verify=False)
logging.captureWarnings(True)#可以通过将警告移到日志的方法来忽略警告
#通过cert来指定证书(crt地址,key地址)key必须是解密状态
print(response.status_code)#按照书中写的这里应该返回ssl证书错误因为12306的证书没有被ca官方机构信任,可以通过更改verify参数设置 忽略证书的检查
