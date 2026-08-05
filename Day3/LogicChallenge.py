# Logic Challenge

import pandas as pd

data = {
    "Name": [
        "A",
        "B",
        "A",
        None,
        "C"
    ],
    "Salary": [
        10000,
        None,
        10000,
        50000,
        None
    ]
}

df=pd.DataFrame(data)

print(df)

# Tasks:

# Count missing values
print(df.isna().sum())

# Fill missing salary with 25000
df["Salary"]=df["Salary"].fillna(25000)

# Remove duplicate rows
df=df.drop_duplicates()

# Remove rows where Name is missing
df["Name"]=df["Name"].drop_duplicates()

print(df)
