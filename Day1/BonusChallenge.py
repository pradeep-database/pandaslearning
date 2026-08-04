# Bonus Challenge

import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D"],
    "Salary": [10000, 20000, 30000, 40000],
    "Department":["IT","BANK","TAILOR","BEAUTICIAN"],
    "Age":[55,28,37,29]
}

sampledataframe=pd.DataFrame(data)

sampledataframe.to_csv("Sampledataframe.csv",index=False)