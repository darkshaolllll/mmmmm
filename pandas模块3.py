import pandas as pd
import numpy as np
a=pd.Series(['xinx','科学',np.nan])
print(a)
print(a.isnull())#为空返回fasle
