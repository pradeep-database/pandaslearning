# Assignment 6 – Department Filter

# Display only employees from:

import pandas as pd

df=pd.read_csv("employees.csv")

print(df[df["Department"]=='Finance'])