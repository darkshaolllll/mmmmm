import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}#键值充当列名
df = pd.DataFrame(data,index=[34,44,55,22])
a=pd.read_excel("C:/Users/52784/Desktop/ii.xlsx")
print(a)
print(df)