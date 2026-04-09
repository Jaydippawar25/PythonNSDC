import pandas as pd
les = [1,2,3,4,5]
srs = pd.Series(les,index=['a','b','c','d','e'])
print(srs.head(3))