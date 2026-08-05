# Assignment 1 – Detect Missing Values

import pandas as pd

df = pd.read_csv("employees_missing.csv")

print(df.isna())