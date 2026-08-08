# Assignment 3 — Inner Join

# Combine employees and departments using department_id.

# Perform an Inner Join.

import pandas as pd

df1=pd.read_csv("employees.csv")
df2=pd.read_csv("departments.csv")

df3=pd.merge(df1,df2,on="department_id")

print(df3)

# Check:

# How many employees are present?

print("employees count",df3["employee_id"].nunique())

# Is Marketing present?

print(df3["department_name"].isin(["Marketing"]))

# Why?

# No, Marketing department is not present since no employee has mapped with that department