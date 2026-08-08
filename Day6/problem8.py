# Merge this with your employee data.

# Your final dataset should contain:

# Employee details
# Department details
# Joining year

import pandas as pd

df1=pd.read_csv("employees.csv")
df2=pd.read_csv("departments.csv")
df3=pd.read_csv("new_datsaset.csv")

print(df1.merge(df2).merge(df3))

