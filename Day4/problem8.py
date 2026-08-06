# Assignment 8 – Rank Employees

import pandas as pd

df = pd.read_csv("employeees.csv")

df["Salary Rank"] = df["Salary"].rank(ascending=False)

print(df)