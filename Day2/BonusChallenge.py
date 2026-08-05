# Bonus Challenge

import pandas as pd

df=pd.read_csv("employees.csv")

salary_df = df["Salary"]

salary_df.to_csv("salary_report.csv",index=False)
