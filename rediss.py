from redis import StrictRedis
redis=StrictRedis(host='localhost',port=1009,db=0,password='root')
redis.set('name','bob')
print(redis.get('name'))