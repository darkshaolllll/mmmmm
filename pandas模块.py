import numpy as np
import pandas as pd
a=np.random.randn(3,5)#生成一个三行五列的二维数组
date1=pd.date_range('20200701',periods=3)
b=pd.DataFrame(a,index=date1)#index指列

print(date1)
print(a)
print(b)