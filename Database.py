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
        self.numRecords = 0
        self.recordSize = 0
        self.dataFileptr = None
        self.name = title
        self.status = False

    def read_record(self, recordNum, passengerId, fname, lname, age, ticketNum, fare, date):
        self.ID = recordNum
        # parse
        # readRecord: a private helper method (it may be public if you need to call it from the main program)
        # parameter(s): recordNum, &passengerId, &fname, &lname, &age, &ticketNum, &fare, &date
        # returns: int (-1 if the recordNum is invalid, 0 if it is valid but is an empty record, 1 the read was successful)
        # purpose: if db is open and recordNum is valid, it seeks to the beginning of recordNum in the already opened file and reads the key, if the key is not _empty_, it reads the rest of the record and fills the parameters.

    def write_record(self, recordNum, passengerId, fname, lname, age, ticketNum, fare, date):
        self.num = recordNum
        # writeRecord: a private helper method (it may be public if you need to call it from the main program)
        # parameter(s): recordNum, passengerId, fname, lname, age, ticketNum, fare, date
        # returns: int (-1 if the recordNum is invalid, 0 if it is valid and we overwrote an empty record, 1 if we overwrote a non-empty record
        # purpose: Using formatted writes, writes a fixed length record at the location indicated by recordNum.

    def update_record(self, passengerId, fname, lname, age, ticketNum, fare, date):
        self.ID = passengerId
    # parameter(s): passengerId, fname, lname, age, ticketNum, fare, date
    # returns: Boolean, true if record is updated, false otherwise
    # purpose: if db is open, it uses binarySearch to locate the record. It then uses writeRecord to overwrite it. NOTE: it assumes that the key (passengerId) will not be changed or binarySearch will break.

    def delete_record(self, passengerId):
        self.ID = passengerId
        # parameter(s): passengerId
        # returns: Boolean, true if record is deleted, false otherwise
        # purpose: if db is open, it uses binarySearch to locate the record. It then uses writeRecord to overwrite it with default (empty) values. It sets the passengerId to _empty_.

    def add_record(self, passengerId, fname, lname, age, ticketNum, fare, date):
        self.ID = passengerId
    # parameter(s): passengerId, fname, lname, age, ticketNum, fare, date
    # returns: Boolean, true if db open, false otherwise
    # purpose: if db is open, it overwrites an empty record in the right location, if it exists. BONUS (10%): If there is no empty record in the right location to use, then it closes the file, rewrites it alternating real and empty records of the same size (including the new record), rewrites the config file with the new number of records, and reopens the database.

    def open_db(self, name):
        self.status = True
        # parameter: name to use
        # returns: boolean of success
        # purpose:open config file to read numRecords and recordSize then closes it again. opens data file in read/write mode and sets dataFileptr to open file, updates values in other instance variables.

    # close the database
    def close_db(self):
        self.numRecords = 0
        self.recordSize = 0
        self.dataFileptr = None
        self.text_filename.close()

    # parameter(s): none
    # returns: nothing
    # purpose: resets instance variables, e.g., sets numRecords and recordSize to 0, closes the datafile, sets dataFileptr to NULL, etc.

    def is_open(self):
        return self.status
        # parameter(s): none
        # returns: Boolean (true if database is Open, false if not)
        # purpose: allow main program to check the status of the DB
