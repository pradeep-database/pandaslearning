# Assignment 5 – Salary Filter

# Show employees whose salary is greater than 50,000.

import pandas as pd

df=pd.read_csv("employees.csv")

print(df[df["Salary"]>50000])