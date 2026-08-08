# 📝 Assignment 7

# Generate a report that contains, for each department:

# Average Salary
# Maximum Salary
# Minimum Salary
# Employee Count

# Try to generate everything in a single operation.

import pandas as pd

df=pd.read_csv("employees.csv")

# Count values using group by

print(df.groupby("Department")["Salary"].agg(["mean","max","min","count"]))