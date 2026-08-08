# Assignment 1

# Group the employee data by Department.

import pandas as pd

df=pd.read_csv("employees.csv")

group=df.groupby("Department")

print(group.groups)