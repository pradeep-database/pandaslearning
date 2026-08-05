# Assignment 5 – dropna()

import pandas as pd

df = pd.read_csv("employees_missing.csv")

print(df.dropna())