# Assignment 9 – Reset Index

import pandas as pd

df = pd.read_csv("employeees.csv")

df["Salary Rank"] = df["Salary"].rank(ascending=False)

print(df["Salary Rank"].sort_values())

df.sort_values(by=["Salary Rank"],inplace=True)

print(df)

df.reset_index(inplace=True)

print(df)