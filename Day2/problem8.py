# Assignment 8 – OR Condition

# Display employees who belong to:

# HR
# IT

import pandas as pd

df=pd.read_csv("employees.csv")

print(df[ (df["Department"]=='HR') | (df["Department"]=='IT')])
