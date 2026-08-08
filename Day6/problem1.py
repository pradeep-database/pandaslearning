# Assignment 1 — Load Multiple Datasets

# Read both CSV files into separate DataFrames.

# Verify:

# Number of rows
# Number of columns
# Column names

import pandas as pd

df1=pd.read_csv("employees.csv")
df2=pd.read_csv("departments.csv")

# To know Number of rows,Number of columns and Column names

print(df1.info())

# To know Number of rows,Number of columns and Column names

print(df2.info())

