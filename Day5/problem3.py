# 📝 Assignment 3

# Find the total salary paid by each department.

import pandas as pd

df=pd.read_csv("employees.csv")

print(df.groupby("Department")["Salary"].sum())