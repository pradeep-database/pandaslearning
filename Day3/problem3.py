# Assignment 3 – notnull()

import pandas as pd

df = pd.read_csv("employees_missing.csv")

print(df["Salary"].notnull())