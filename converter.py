import pandas as pd

class converter:
    # recordSize: the number of bytes in a record
    # numRecords: the number of sorted records in the .data file
    # dataFileptr: the fileptr for the opened data file
    # any others you want

    # default constructor
    def __init__(self, title):
        csv_name = title +".csv"
        self.df = pd.read_csv(csv_name,sep=',', header = None)
        # df.to_csv('SmallTitanic.csv',header=None)
        self.df.columns = ['ID', 'FIRST_NAME', 'LAST_NAME', 'AGE', 'TICKET_NUM', 'FARE', 'DATE_OF_PURCHASE']
        # print(self.df)
    
    def get_df(self):
        return self.df