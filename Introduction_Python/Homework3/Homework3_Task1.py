import os
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Step 1-iig hylbar argaar edit hiiv

df = pd.read_excel("./UnurtuvshinHomework/Homework3/data.xlsx")

Task1Step2 = df[(df["age"] > 25) & (df["gender"] == "F")]
Task1Step2['id'] = np.arange(1, len(Task1Step2)+1)
Task1Step2.to_csv(
    './UnurtuvshinHomework/Homework3/Task1Step2.csv', index=False)

# End of Step 2

Task1Step3 = df[(df["age"] < 23) & (df["gender"] == "M")]
Task1Step3['id'] = np.arange(1, len(Task1Step3)+1)
Task1Step3.to_csv(
    './UnurtuvshinHomework/Homework3/Task1Step3.json', index=False)

# End of Step 3
