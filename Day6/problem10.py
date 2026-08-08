# Assignment 10 — Column-wise concat()

# Create:

# DataFrame A

# Employee ID + Name

# DataFrame B

# Employee ID + Salary

# Combine them column-wise.

# Observe what happens to the index and Employee ID.

# This assignment is specifically to understand the difference between:

# row-wise concat vs column-wise concat

import pandas as pd

df1=pd.read_csv("empid_name.csv")
df2=pd.read_csv("empid_salary.csv")

df3=pd.concat([df1,df2],axis=1)

print(df3)