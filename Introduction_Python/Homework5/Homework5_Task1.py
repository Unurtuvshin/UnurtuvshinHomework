# Homework 5 Control Flow Task 1 Step 1, 2

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_excel("./UnurtuvshinHomework/Introduction_Python/Homework5/data.xlsx")

Task1Step1 = pd.DataFrame(columns = df.columns.values.tolist())

for index, row in df.iterrows():
    if((row["age"] > 25) & (row["gender"] == "F")):
        Task1Step1.loc[len(Task1Step1.index)] = row

Task1Step1['id'] = np.arange(1, len(Task1Step1)+1)

Task1Step1.to_csv(
    './UnurtuvshinHomework/Introduction_Python/Homework5/Task1Step1.csv', index=False)

# End of Step 1

Task1Step2 = pd.DataFrame(columns = df.columns.values.tolist())

for index, row in df.iterrows():
    if((row["age"] < 23) & (row["gender"] == "M")):
        Task1Step2.loc[len(Task1Step2.index)] = row

Task1Step2['id'] = np.arange(1, len(Task1Step2)+1)

Task1Step2.to_json(
    './UnurtuvshinHomework/Introduction_Python/Homework5/Task1Step2.json')

# End of Step 2