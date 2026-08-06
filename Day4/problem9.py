# Assignment 9 – Reset Index

import pandas as pd

df = pd.read_csv("employeees.csv")

df["Salary Rank"] = df["Salary"].rank(ascending=False)

df.sort_values(by=["Salary Rank"],inplace=True)

df.reset_index(inplace=True)

print(df)