# Assignment 2 — Understand the Relationship

# Identify:

# Employees → Departments

# Which column connects the two datasets?

# department_id is the brigde between the datasets

import pandas as pd

df1=pd.read_csv("employees.csv")
df2=pd.read_csv("departments.csv")

print(pd.merge(df1,df2,on="department_id"))

# Write down:

# Employee table key = ?
# employee_id is the pk for Employee table

# Department table key = ?
# department_id is the pk for Employee table


