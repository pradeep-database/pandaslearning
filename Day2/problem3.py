# Assignment 3 – Select Rows Using iloc

# Print:

# First row
# First 3 rows
# Rows 2 to 5

import pandas as pd

df=pd.read_csv("employees.csv")

# First row
print(df.iloc[0])

# First 3 rows
print(df.iloc[0:3])

# Rows 2 to 5
print(df.iloc[2:5])