# Assignment 10

# Prepare a business report containing:

import pandas as pd

df=pd.read_csv("employees.csv")


print(df.groupby("Department").agg(
    Employees=("Salary","count"),
    AverageSalary=("Salary","mean"),
    HighestSalary=("Salary","max")
    ))