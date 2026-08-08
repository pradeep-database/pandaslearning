# 📝 Assignment 9

# After creating a grouped report:

# Convert the grouped result back into a normal DataFrame.
# Observe how the output changes.

import pandas as pd

df=pd.read_csv("employees.csv")

# Count values using group by

new_df=df.groupby("Department").agg({"Salary":"mean","Experience":"mean"})

print(new_df)