from scipy.io import arff
import pandas as pd

data = arff.loadarff('speeddating.arff')
df = pd.DataFrame(data[0])
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print("Number of missing values: ")
print(df.isnull().sum())
print(df.describe())

for attribute in df.columns:
    if df[attribute].dtype == 'object':
        df[attribute] = df[attribute].str.decode('utf-8')

df.to_csv('speeddating.csv', index=False)
