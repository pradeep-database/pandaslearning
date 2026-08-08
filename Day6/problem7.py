# Assignment 7 — Select Required Columns

# After joining the datasets, create a final employee report containing only:

# Employee ID
# Employee Name
# Department Name
# Location
# Salary

# No unnecessary columns.

import pandas as pd

df1=pd.read_csv("employees.csv")
df2=pd.read_csv("departments.csv")

df3=pd.merge(df1,df2,on="department_id")

print(df3[["employee_id","name","department_name","location","salary"]])