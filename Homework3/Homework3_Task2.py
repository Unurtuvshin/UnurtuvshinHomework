import os
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_excel("./UnurtuvshinHomework/Homework3/data.xlsx")

Step1 = df.iloc[17:18, 2:6]
Step1

# End of Step 1

Step2 = df.loc[25:28, ("firstName", "age")]
Step2

# End of Step 2

df.groupby('gender')[['salary', 'age']].min()
df.groupby('gender')[['salary', 'age']].max()
df.groupby('gender')[['salary', 'age']].mean()

# End of Step 3

Step4_min = pd.pivot_table(df, values=['salary', 'age'], index=[
                           'gender'], aggfunc=np.min)
Step4_min

Step4_max = pd.pivot_table(df, values=['salary', 'age'], index=[
                           'gender'], aggfunc=np.max)
Step4_max

Step4_mean = pd.pivot_table(df, values=['salary', 'age'], index=[
                            'gender'], aggfunc=np.mean)
Step4_mean

# End of Step 4
