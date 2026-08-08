# Assignment 5 — Right Join

# Perform a Right Join where departments are the right DataFrame.

import pandas as pd

df1=pd.read_csv("employees.csv")
df2=pd.read_csv("departments.csv")

df3=pd.merge(df1,df2,on="department_id",how="right")

print(df3)

# Check:

# Does Marketing appear?

# Yes, since we used right join marketing is found

# What values does Marketing have for employee-related columns?

# NaN will have since no employee mapped with that department