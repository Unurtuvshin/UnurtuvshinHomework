import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_excel("./UnurtuvshinHomework/Introduction_Python/Homework5/data.xlsx")

fname = df['firstName'].tolist()
lname = df['lastName'].tolist()

# Step 1 - fname, lname - zip

for i in zip(fname, lname):
    print(i)

#Step 2 - enumerate fname

obj1 = enumerate(fname)
for i in obj1:
    print(i[0], i[1])