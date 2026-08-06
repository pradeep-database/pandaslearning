# Assignment 10 – Top 3 Highest Paid Employees

import pandas as pd

df = pd.read_csv("employeees.csv")

df["Salary Rank"] = df["Salary"].rank(ascending=False)

df.sort_values(by=["Salary Rank"],inplace=True)

print(df[["Name","Department","Salary"]].head(3))
