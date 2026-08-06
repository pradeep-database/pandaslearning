# Assignment 2 – Sort Salary (Descending)

import pandas as pd

df = pd.read_csv("employeees.csv")

print(df.sort_values("Salary",ascending=False))