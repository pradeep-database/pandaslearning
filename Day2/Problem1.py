# Assignment 1 – Select One Column

# Print only the Name column.

import pandas as pd

df=pd.read_csv("employees.csv")

print(df["Name"])