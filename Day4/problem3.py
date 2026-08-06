# Assignment 3 – Sort by Multiple Columns

# Sort using:

# Department
# Salary (Descending)

import pandas as pd

df = pd.read_csv("employeees.csv")

print(df.sort_values(by=["Department","Salary"],ascending=[True,False]))