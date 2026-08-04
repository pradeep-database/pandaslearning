# Logic Challenge

import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D"],
    "Salary": [10000, 20000, 30000, 40000]
}

sampledataframe=pd.DataFrame(data)

print(sampledataframe.describe())