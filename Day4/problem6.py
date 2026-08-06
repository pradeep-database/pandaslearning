# Assignment 6 – unique()

import pandas as pd

df = pd.read_csv("employeees.csv")

print(df["Department"].unique())