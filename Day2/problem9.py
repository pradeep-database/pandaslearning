# Assignment 9 – isin()

import pandas as pd

df=pd.read_csv("employees.csv")

print(df[df["Department"].isin(["HR","Finance"])])