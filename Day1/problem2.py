# Assignment 2 – First 5 Rows

import pandas as pd

dataframe=pd.read_csv("Day1/employees.csv")

print(dataframe.head())

print(dataframe.head(3))
