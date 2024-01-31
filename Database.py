import csv
import os.path


class DB:
    # recordSize: the number of bytes in a record
    # numRecords: the number of sorted records in the .data file
    # dataFileptr: the fileptr for the opened data file
    # any others you want

    # default constructor
    def __init__(self):
        # parameter(s): none
        # returns: nothing
        # purpose: inits instance variables, e.g., sets numRecords and recordSize to 0, dataFileptr to NULL
        self.numRecords = 0
        self.recordSize = 0
        self.dataFileptr = None

    # # create database
    # def createDB(self, filename):
    #     # Generate file names
    #     csv_filename = filename + ".csv"
    #     text_filename = filename + ".data"
    #
    #     # Read the CSV file and write into data files
    #     with open(csv_filename, "r") as csv_file:
    #         data_list = list(csv.DictReader(csv_file, fieldnames=('ID', 'experience', 'marriage', 'wages', 'industry')))
    #
    #     # Formatting files with spaces so each field is fixed length, i.e. ID field has a fixed length of 10
    #     def writeDB(filestream, dict):
    #         filestream.write("{:{width}.{width}}".format(dict["ID"], width=self.Id_size))
    #         filestream.write("{:{width}.{width}}".format(dict["experience"], width=self.Experience_size))
    #         filestream.write("{:{width}.{width}}".format(dict["marriage"], width=self.Marriage_size))
    #         filestream.write("{:{width}.{width}}".format(dict["wages"], width=self.Wage_size))
    #         filestream.write("{:{width}.{width}}".format(dict["industry"], width=self.Industry_size))
    #         filestream.write("\n")
    #
    #     # write an empty records
    #     # filestream.write("{:{width}.{width}}".format('_empty_',width=self.Id_size))
    #     # filestream.write("{:{width}.{width}}".format(' ',width=self.Experience_size))
    #     # filestream.write("{:{width}.{width}}".format(' ',width=self.Marriage_size))
    #     # filestream.write("{:{width}.{width}}".format(' ',width=self.Wage_size))
    #     # filestream.write("{:{width}.{width}}".format(' ',width=self.Industry_size))
    #     # filestream.write("\n")
    #
    #     with open(text_filename, "w") as outfile:
    #         for dict in data_list:
    #             writeDB(outfile, dict)

    # #read the database
    # def readDB(self, filename, DBsize, rec_size):
    #     self.filestream = filename + ".data"
    #     self.record_size = DBsize
    #     self.rec_size = rec_size

    #     if not os.path.isfile(self.filestream):
    #         print(str(self.filestream)+" not found")
    #     else:
    #         self.text_filename = open(self.filestream, 'r+')

    # #read record method
    # def getRecord(self, recordNum):

    #     self.flag = False
    #     id = experience = marriage = wage = industry = "None"

    #     if recordNum >=0 and recordNum < self.record_size:
    #         self.text_filename.seek(0,0)
    #         self.text_filename.seek(recordNum*self.rec_size)
    #         line= self.text_filename.readline().rstrip('\n')
    #         self.flag = True

    #     if self.flag:
    #         id = line[0:10]
    #         experience = line[10:15]
    #         marriage = line[15:20]
    #         wage = lifne[20:40]
    #         industry = line[40:70]
    #         self.record = dict({"ID":id,"experience":experience,"marriage":marriage,"wages":wage,"industry":industry})

    def readRecord(self, recordNum, passengerId, fname, lname, age, ticketNum, fare, date):

        # readRecord: a private helper method (it may be public if you need to call it from the main program)
        # parameter(s): recordNum, &passengerId, &fname, &lname, &age, &ticketNum, &fare, &date
        # returns: int (-1 if the recordNum is invalid, 0 if it is valid but is an empty record, 1 the read was successful)
        # purpose: if db is open and recordNum is valid, it seeks to the beginning of recordNum in the already opened file and reads the key, if the key is not _empty_, it reads the rest of the record and fills the parameters.

    def writeRecord(self, recordNum, passengerId, fname, lname, age, ticketNum, fare, date):

        # writeRecord: a private helper method (it may be public if you need to call it from the main program)
        # parameter(s): recordNum, passengerId, fname, lname, age, ticketNum, fare, date
        # returns: int (-1 if the recordNum is invalid, 0 if it is valid and we overwrote an empty record, 1 if we overwrote a non-empty record
        # purpose: Using formatted writes, writes a fixed length record at the location indicated by recordNum.

    def updateRecord(self, passengerId, fname, lname, age, ticketNum, fare, date):

    # parameter(s): passengerId, fname, lname, age, ticketNum, fare, date
    # returns: Boolean, true if record is updated, false otherwise
    # purpose: if db is open, it uses binarySearch to locate the record. It then uses writeRecord to overwrite it. NOTE: it assumes that the key (passengerId) will not be changed or binarySearch will break.

    def deleteRecord(self, passengerId):
        # parameter(s): passengerId
        # returns: Boolean, true if record is deleted, false otherwise
        # purpose: if db is open, it uses binarySearch to locate the record. It then uses writeRecord to overwrite it with default (empty) values. It sets the passengerId to _empty_.

    def addRecord(self, passengerId, fname, lname, age, ticketNum, fare, date):

    # parameter(s): passengerId, fname, lname, age, ticketNum, fare, date
    # returns: Boolean, true if db open, false otherwise
    # purpose: if db is open, it overwrites an empty record in the right location, if it exists. BONUS (10%): If there is no empty record in the right location to use, then it closes the file, rewrites it alternating real and empty records of the same size (including the new record), rewrites the config file with the new number of records, and reopens the database.

    # # Binary Search by record id
    # def binarySearch(self, input_ID):
    #     # parameter(s): passengerId, &recordNum, &fname, &lname, &age, &ticketNum, &fare, &date
    #     # returns: Boolean, true if the passengerId was found, false if not
    #     # purpose: if db open, it uses seeks to perform binary search on the sorted file to locate the id. It fills in the parameters with the data (if found), otherwise it sets them to default values. recordNum is set to the location where the record would be, if it was in the datafile
    #     low = 0
    #     high = self.record_size - 1
    #     found = False
    #     self.recordNum = None  # Initialize the insertion point
    #
    #     while not found and high >= low:
    #         self.middle = (low + high) // 2
    #         self.getRecord(self.middle)
    #         mid_id = self.record["ID"]
    #
    #         if mid_id.strip() == "_empty_":
    #             non_empty_record = self.findNearestNonEmpty(self.middle, low, high)
    #             if non_empty_record == -1:
    #                 # If no non-empty record found, set recordNum for potential insertion
    #                 self.recordNum = high
    #                 print("Could not find record with ID..", input_ID)
    #                 return False
    #
    #             self.middle = non_empty_record
    #             self.getRecord(self.middle)
    #             mid_id = self.record["ID"]
    #             if int(mid_id) > int(input_ID):
    #                 self.recordNum = self.middle - 1
    #             else:
    #                 self.recordNum = self.middle + 1
    #
    #         if mid_id != "_empty_":
    #             try:
    #                 if int(mid_id) == int(input_ID):
    #                     found = True
    #                     self.recordNum = self.middle
    #                 elif int(mid_id) > int(input_ID):
    #                     high = self.middle - 1
    #                 elif int(mid_id) < int(input_ID):
    #                     low = self.middle + 1
    #             except ValueError:
    #                 # Handle non-integer IDs
    #                 high = self.middle - 1
    #
    #     if not found and self.recordNum is None:
    #         # Set recordNum to high + 1 if no suitable spot is found
    #         self.recordNum = high
    #         print("Could not find record with ID", input_ID)
    #
    #     return found
    #
    # def findNearestNonEmpty(self, start, low_limit, high_limit):
    #     step = 1  # Initialize step size
    #
    #     while True:
    #         # Check backward
    #         if start - step >= low_limit:
    #             self.getRecord(start - step)
    #             if self.record["ID"].strip() != "_empty_":
    #                 # print(self.record)
    #                 return start - step
    #
    #         # Check forward
    #         if start + step <= high_limit:
    #             self.getRecord(start + step)
    #             if self.record["ID"].strip() != "_empty_":
    #                 # print(self.record)
    #                 return start + step
    #
    #         # Increase step size and repeat
    #         step += 1
    #
    #         # Terminate if beyond the search range
    #         if start - step < low_limit and start + step > high_limit:
    #             break
    #
    #     return -1  # No non-empty record found

    def OpenDB(self, name):
        # parameter: name to use
        # returns: boolean of success
        # purpose:open config file to read numRecords and recordSize then closes it again. opens data file in read/write mode and sets dataFileptr to open file, updates values in other instance variables.

    # close the database
    def CloseDB(self):
        self.text_filename.close()

    # parameter(s): none
    # returns: nothing
    # purpose: resets instance variables, e.g., sets numRecords and recordSize to 0, closes the datafile, sets dataFileptr to NULL, etc.

    def isOpen(self):
        # parameter(s): none
        # returns: Boolean (true if database is Open, false if not)
        # purpose: allow main program to check the status of the DB
