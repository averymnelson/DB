import csv
import os.path

# ID, fname, lname, age, ticketnum, fare, purchased
class DB:
    # recordSize: the number of bytes in a record
    # numRecords: the number of sorted records in the .data file
    # dataFileptr: the fileptr for the opened data file
    # any others you want

    # default constructor
    def __init__(self, title):
        # parameter(s): none
        # returns: nothing
        # purpose: inits instance variables, e.g., sets numRecords and recordSize to 0, dataFileptr to NULL
        self.filestream = None
        self.numRecords = 0
        self.idsize =0
        self.fnamesize = 0
        self.lnamesize = 0
        self.agesize = 0
        self.ticketnumsize = 0
        self.faresize = 0
        self.purchasesize = 0

    def read_src(self, name):
        csv_filename = name +".csv"
        text_filename = name + ".txt"
        with open(csv_filename, "r") as csv_file:
            data_list = list(csv.DictReader(csv_file, fieldnames= ('PASSENGER_ID', 'FIRST_NAME', 'LAST_NAME', 'AGE', 'TICKET_NUM', 'FARE', 'DATE_OF_PURCHASE')))

        def write_src(filestream, dict):
            filestream.write("{:{width}.{width}}".format(dict["PASSENGER_ID"], width=self.idsize))
            filestream.write("{:{width}.{width}}".format(dict["FIRST_NAME"], width=self.fnamesize))
            filestream.write("{:{width}.{width}}".format(dict["LAST_NAME"], width=self.lnamesize))
            filestream.write("{:{width}.{width}}".format(dict["AGE"], width=self.agesize))
            filestream.write("{:{width}.{width}}".format(dict["TICKET_NUM"], width=self.ticketnumsize))
            filestream.write("{:{width}.{width}}".format(dict["FARE"], width=self.faresize))
            filestream.write("{:{width}.{width}}".format(dict["DATE_OF_PURCHASE"], width=self.purchasesize))
            filestream.write("\n")


        with open(text_filename,"w") as outfile:
            for dict in data_list:
                write_src(outfile,dict)

    def read_record(self, recordnum):
        self.flag = False
        id = experience = marriage = wage = industry = "None"

        if recordnum >= 0 and recordnum < self.record_size:
            self.text_filename.seek(0, 0)
            self.text_filename.seek(recordnum * self.rec_size)
            line = self.text_filename.readline().rstrip('\n')
            self.flag = True

        if self.flag:
            id = line[0:10]
            experience = line[10:15]
            marriage = line[15:20]
            wage = line[20:40]
            industry = line[40:70]
            self.record = dict(
                {"ID": id, "experience": experience, "marriage": marriage, "wages": wage, "industry": industry})

        # parse
        # readRecord: a private helper method (it may be public if you need to call it from the main program)
        # parameter(s): recordNum, &passengerid, &fname, &lname, &age, &ticketnum, &fare, &date
        # returns: int (-1 if the recordNum is invalid, 0 if it is valid but is an empty record, 1 the read was successful)
        # purpose: if db is open and recordNum is valid, it seeks to the beginning of recordNum in the already opened file and reads the key, if the key is not _empty_, it reads the rest of the record and fills the parameters.

    def write_record(self, recordnum, passengerid, fname, lname, age, ticketnum, fare, date):
        self.num = recordnum
        # writeRecord: a private helper method (it may be public if you need to call it from the main program)
        # parameter(s): recordNum, passengerid, fname, lname, age, ticketnum, fare, date
        # returns: int (-1 if the recordNum is invalid, 0 if it is valid and we overwrote an empty record, 1 if we overwrote a non-empty record
        # purpose: Using formatted writes, writes a fixed length record at the location indicated by recordNum.

    def update_record(self, passengerid, fname, lname, age, ticketnum, fare, date):
        self.ID = passengerid
    # parameter(s): passengerid, fname, lname, age, ticketnum, fare, date
    # returns: Boolean, true if record is updated, false otherwise
    # purpose: if db is open, it uses binarySearch to locate the record. It then uses writeRecord to overwrite it. NOTE: it assumes that the key (passengerid) will not be changed or binarySearch will break.

    def delete_record(self, passengerid):
        self.ID = passengerid
        # parameter(s): passengerid
        # returns: Boolean, true if record is deleted, false otherwise
        # purpose: if db is open, it uses binarySearch to locate the record. It then uses writeRecord to overwrite it with default (empty) values. It sets the passengerid to _empty_.

    def add_record(self, passengerid, fname, lname, age, ticketnum, fare, date):
        self.ID = passengerid
    # parameter(s): passengerid, fname, lname, age, ticketnum, fare, date
    # returns: Boolean, true if db open, false otherwise
    # purpose: if db is open, it overwrites an empty record in the right location, if it exists. BONUS (10%): If there is no empty record in the right location to use, then it closes the file, rewrites it alternating real and empty records of the same size (including the new record), rewrites the config file with the new number of records, and reopens the database.

    def read_db(self, name, DBsize, rec_size):
        self.filestream = name + ".data"
        self.record_size = DBsize
        self.rec_size = rec_size

        if not os.path.isfile(self.filestream):
            print(str(self.filestream) + " not found")
        else:
            self.text_filename = open(self.filestream, 'r+')
        # parameter: name to use
        # returns: boolean of success
        # purpose:open config file to read numRecords and recordSize then closes it again. opens data file in read/write mode and sets dataFileptr to open file, updates values in other instance variables.

    # close the database
    def close_db(self):
        self.text_filename.close()

    # parameter(s): none
    # returns: nothing
    # purpose: resets instance variables, e.g., sets numRecords and recordSize to 0, closes the datafile, sets dataFileptr to NULL, etc.