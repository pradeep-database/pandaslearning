# Assignment 6 – replace()

import pandas as pd

df = pd.read_csv("employees_missing.csv")

print(df.replace("HR","Human Resources"))