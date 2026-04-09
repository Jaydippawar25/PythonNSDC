import pandas as pd
dict = {
    'Name':['Ram','Sham','Sita','Gita'],
    'age':[20,22,19,18],
    'city':['Pune','Mumbai',pd.NA,'Kokan']
}
df = pd.DataFrame(dict )

# print(df)
print(df[0:3])
# print(df['age'])