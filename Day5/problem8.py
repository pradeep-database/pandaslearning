# 📝 Assignment 8

# For every department, calculate:

# Average Salary
# Average Experience

# Display both in one report.

import pandas as pd

df=pd.read_csv("employees.csv")

# Count values using group by

print(df.groupby("Department").agg({"Salary":"mean","Experience":"mean"}))

