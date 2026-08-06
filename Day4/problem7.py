# Assignment 7 – nunique()

import pandas as pd

df = pd.read_csv("employeees.csv")

print(df["Department"].nunique())