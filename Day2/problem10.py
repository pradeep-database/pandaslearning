# Assignment 10 – between()

import pandas as pd

df=pd.read_csv("employees.csv")

print(df[df["Salary"].between(20000,70000) ])