# Assignment 10 – Save Clean Data

import pandas as pd

# Read CSV
df = pd.read_csv("employees_missing.csv")
# Fill missing Salary with 30000

df["Salary"]=df["Salary"].fillna(30000)

# Fill missing Experience with 0

df["Experience"]=df["Experience"].fillna(0)

# Replace HR → Human Resources

df["Department"]=df["Department"].replace("HR","Human Resources")

# Remove duplicates

df.drop_duplicates(inplace=True)

# cleaned DataFrame to save

df.to_csv("employees_cleaned.csv",index=False)

