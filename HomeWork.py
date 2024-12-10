import pandas as pd

df = pd.read_csv('final_scout_not_dummy.csv')

print(df.head())
print(df.info())
print(df.describe())

df = pd.read_csv('dz.csv')

mid_salary = df.groupby('City')['Salary'].mean()
print(mid_salary)