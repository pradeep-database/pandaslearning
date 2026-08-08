# Assignment 4 — Left Join

# Perform a Left Join where employees are the left DataFrame.

import pandas as pd

df1=pd.read_csv("employees.csv")
df2=pd.read_csv("departments.csv")

df3=pd.merge(df1,df2,on="department_id",how="left")

print(df3)

# Check:

# Are all employees present?

# actual employee count
actual_empcount=df1["employee_id"].nunique()

# new dataframe employee count
new_dfempcount=df3["employee_id"].nunique()

print("Yes all are present" if actual_empcount==new_dfempcount else "No,Not all are present")

# What happens if an employee has an unknown department?

# The department value result will have NaN for that employee

# Does Marketing appear?

print(df3["department_name"].isin(["Marketing"]))

# No, Marketing department is not present since no employee has mapped with that department

