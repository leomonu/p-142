import pandas as pd
import numpy as np

df = pd.read_csv("Articles.csv")

df = df.sort_values(["total_events"],ascending = [False])
# print(df.head())

output = df[["url","title","text","lang","total_events"]].head(10).values.tolist()
# print(output)