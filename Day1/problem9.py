# Assignment 9 – Create DataFrame from Dictionary

import pandas as pd

data = {
    "Name": ["Rahul", "Ajay", "Kiran"],
    "Age": [25, 28, 30],
    "Department": ["IT", "Finance", "HR"]
}

sampledataframe = pd.DataFrame(data)

print(sampledataframe)