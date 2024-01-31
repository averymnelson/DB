import pandas as pd

df = pd.read_csv("input.txt",sep=',', header = None)
df.to_csv('SmallTitanic.csv',header=None)