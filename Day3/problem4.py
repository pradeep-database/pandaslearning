# Assignment 4 – fillna()

import pandas as pd

df = pd.read_csv("employees_missing.csv")

print(df["Salary"].fillna(3000))