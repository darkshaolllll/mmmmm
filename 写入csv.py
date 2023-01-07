import csv
import pandas as pd
with open('data1.csv','w',encoding='utf-8') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['1001','mike',20])
with open('data1.csv','w',encoding='utf-8') as csvfile:
    fieldnames=['id','name','age']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'1011','name':'mike','age':22})
df=pd.DataFrame(
    [{'id':'1011','name':'mike','age':22},
    {'id':'1011','name':'mike','age':22}]
)
df.to_csv('data.csv',index=False)