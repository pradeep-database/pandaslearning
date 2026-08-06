# Assignment 1 – Sort Salary (Ascending)

# Sort employees by salary (lowest → highest).

import pandas as pd

df = pd.read_csv("employeees.csv")

print(df.sort_values("Salary"))