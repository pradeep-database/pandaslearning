# 📝 Assignment 5

# Find the highest salary in every department.

import pandas as pd

df=pd.read_csv("employees.csv")

# Count values using group by

print(df.groupby("Department")["Salary"].max())