import pymysql
db=pymysql.connect(host='localhost',user='root',password='root',port=3306)
cursor=db.cursor()
sql='CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY(id))'
data={'id':'2012001','name':'bob','age':20}

table='students'
keys=', '.join(data.keys())
Values=', '.join(['%s']*len(data))
sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=Values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()

