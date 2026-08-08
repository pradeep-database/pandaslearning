# Assignment 6 — Outer Join

# Perform a Full Outer Join.

import pandas as pd

df1=pd.read_csv("employees.csv")
df2=pd.read_csv("departments.csv")

df3=pd.merge(df1,df2,on="department_id",how="outer")

print(df3)

# Your goal is to understand:

# What records exist in either dataset, regardless of whether they match?

# 6th index exists , even no employee mapped with Marketing department the output has the marketing result

# Identify:

# Matched records

# 6 rows are matched

# Unmatched employee records

# 1 record -- marketing

# Unmatched department records

# 1 record -- marketing