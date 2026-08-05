# Assignment 8 – drop_duplicates()

import pandas as pd

df = pd.read_csv("employees_missing.csv")

#  for all rows
print(df.drop_duplicates())

# with single column
print(df.drop_duplicates(subset=["Name"]))