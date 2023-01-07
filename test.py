
import pymysql
db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='lll')
cursor = db.cursor()
data = {
    'id': '20120011',
    'name': 'Bo',
    'age': 65
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
   if cursor.execute(sql, tuple(data.values())):
       print('Successful')
       db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
#还得不存在
