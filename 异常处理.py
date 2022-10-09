from urllib import request,error, response
try:
    response=request.urlopen('https://sdasd.com/index.htm')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')