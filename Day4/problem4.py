# Assignment 4 – Sort by Index

import pandas as pd

df = pd.read_csv("employeees.csv")

df = df.sample(frac=1)

print(df.sort_index())