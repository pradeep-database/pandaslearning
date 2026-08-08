# 📝 Assignment 4

# Count the number of employees in each department.

import pandas as pd

df=pd.read_csv("employees.csv")

# Count values using group by

print(df.groupby("Department")["Salary"].count())

# count values using values_count

print(df["Department"].value_counts())

# group by count check only not Nan Values meanwhile value_Counts counts all
