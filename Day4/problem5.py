# Assignment 5 – value_counts()

# Count employees in each department.

import pandas as pd

df = pd.read_csv("employeees.csv")

print(df["Department"].value_counts())