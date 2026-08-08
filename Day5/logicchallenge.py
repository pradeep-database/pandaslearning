# Logic Challenge

import pandas as pd

df=pd.read_csv("employees.csv")

# Department with the highest average salary.

print(df.groupby("Department")["Salary"].mean().sort_values(ascending=False).head(1))

# Department with the lowest average salary.

print(df.groupby("Department")["Salary"].mean().sort_values().head(1))

# Department paying the highest total salary.

print(df.groupby("Department")["Salary"].sum().sort_values(ascending=False).head(1))

# Department having the most experienced employees on average.

print(df.groupby("Department")["Experience"].mean().sort_values(ascending=False).head(1))
