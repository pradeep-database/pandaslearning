# Assignment 7 – duplicated()

import pandas as pd

df = pd.read_csv("employees_missing.csv")

print(df[df.duplicated()])