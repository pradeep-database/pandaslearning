# Assignment 2 – Select Multiple Columns

# Print:

# Name
# Salary

import pandas as pd

df=pd.read_csv("employees.csv")

print(df[["Name","Salary"]])