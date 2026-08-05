# Assignment 4 – Select Rows Using loc

# Print:

# Row with index 2
# Rows 2 to 5
# Name and Salary columns for rows 2–5

import pandas as pd

df=pd.read_csv("employees.csv")

# Row with index 2

print(df.loc[2])

# Rows 2 to 5

print(df.loc[2:5])

# Name and Salary columns for rows 2–5

print(df.loc[2:5,["Name","Salary"]])