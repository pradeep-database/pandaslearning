# Assignment 7 – Multiple Conditions

# Display employees:

# Salary > 30,000
# Experience >= 2

import pandas as pd

df=pd.read_csv("employees.csv")

print(df[ (df["Salary"]>30000) & (df["Experience"]>=2)])