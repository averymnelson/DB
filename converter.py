import pandas as pd

df = pd.read_csv("SmallTitanic.csv",sep=',', header = None)
# df.to_csv('SmallTitanic.csv',header=None)
df.columns = ['PASSENGER_ID', 'FIRST_NAME', 'LAST_NAME', 'AGE', 'TICKET_NUM', 'FARE', 'DATE_OF_PURCHASE']
print(df)