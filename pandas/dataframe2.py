import pandas as pd

df = pd.read_csv('data1.csv')
# print(df)
# print(df.isna().sum()) # disply null values
# print(df.describe())
# print(df.info())
# print(df.head()) # starting 5 value
# print(df.tail())  # end 5 value
# print(df.columns)
# print(df.shape)
# print(df.dtypes)
# print(df.nunique())
# df2 = df[['age', 'marks' ]]
# print(df2.corr())
# print(df['name'].value_counts())
# print(df['age'].unique())
# print(df['marks'].nunique())
# print(df['grade'].isna().sum()) # check in the grade null values

df['grade'] = df ['grade'].fillna(value='0',inplace=True)
print(df)
# df1 = df['grade'].dropna()
# print(df1)