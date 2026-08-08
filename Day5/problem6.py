# 📝 Assignment 6

# Find the lowest salary in every department.

import pandas as pd

df=pd.read_csv("employees.csv")

# Count values using group by

print(df.groupby("Department")["Salary"].min())