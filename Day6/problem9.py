# Assignment 9 — concat()

# Create two DataFrames representing:

# January Employees

# Employees 101, 102, 103

# February Employees

# Employees 104, 105, 106

# Combine them into one DataFrame using row-wise concatenation.

# Then verify the final number of rows.

import pandas as pd

df1=pd.read_csv("january.csv")
df2=pd.read_csv("feburary.csv")

df3=pd.concat([df1,df2],ignore_index=True)

print(df3)

# To check dataframe details

print(df3.info())

