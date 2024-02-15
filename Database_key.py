#-----------------------------
# HW1 Part 1 solution by Ananya Vangoor and Susan Gauch
#-----------------------------

import csv
import os.path

class DB:

    #default constructor
    def __init__(self):
        self.filestream = None
        self.num_records = 0
        self.record_size = 0
        self.fileptr = None

    #create database
    def createDB(self,filename):
        #Generate file names
        csv_filename = filename + ".csv"
        text_filename = filename + ".data"
        config_filename = filename + ".config"
        
        # Read the CSV file and write into data files
        with open(csv_filename, "r") as csv_file:
            data_list = list(csv.DictReader(csv_file,fieldnames=('ID','first_name','last_name','age','ticket_num', 'fare', 'date_of_purchase')))

        
		# Formatting files with spaces so each field is fixed length, i.e. ID field has a fixed length of 86
        def writeDB(filestream, dict):
            filestream.write("{:5.5}".format(dict["ID"]))
            filestream.write("{:15.15}".format(dict["first_name"]))
            filestream.write("{:20.20}".format(dict["last_name"]))
            filestream.write("{:5.5}".format(dict["age"]))
            filestream.write("{:20.20}".format(dict["ticket_num"]))
            filestream.write("{:5.5}".format(dict["fare"]))
            filestream.write("{:15.15}".format(dict["date_of_purchase"]))
            filestream.write("\n")

        count = 0
        with open(text_filename,"w") as outfile:
            for dict in data_list:
                writeDB(outfile,dict)
                emptyRecord = {"ID": "0", "first_name": "Null", "last_name": "Null", "age": "0", "ticket_num": "0", "fare": "0", "date_of_purchase": "Null"}
                writeDB(outfile, emptyRecord)
                count += 2

        # Opening a config file for writing details
        self.num_records = count
        self.record_size = 86
        config_fileptr = open(config_filename, "w")
        config_fileptr.write(str(self.num_records) + "\n")
        config_fileptr.write(str(self.record_size) + "\n")
        config_fileptr.close()

    #seeking to a specific record method
    def getRecord(self, recordNum):

        self.flag = False
        ID = first_name = last_name = age = ticket_num = fare = date_of_purchase = "None"

        if recordNum >=0 and recordNum < self.num_records:
            self.fileptr.seek(0,0)
            self.fileptr.seek(recordNum*self.record_size)
            line = self.fileptr.readline().rstrip('\n')
            self.flag = True
        else:
            print("You are going out of bounds. You will see an empty record. Choose something between 0 and 19.")
            self.flag = False
            self.record = dict({"ID": "0", "first_name": "Null", "last_name": "Null", "age": "0", "ticket_num": "0", "fare": "0", "date_of_purchase": "Null"})
        
        if self.flag:
            ID = line[0:5]
            first_name = line[5:20]
            last_name = line[20:40]
            age = line[40:45]
            ticket_num = line[45:65]
            fare = line[65:70]
            date_of_purchase = line[70:85]
            self.record = dict({"ID":ID,"first_name":first_name,"last_name":last_name,"age":age,"ticket_num":ticket_num, "fare": fare, "date_of_purchase": date_of_purchase})

    #Binary Search by record id
    def binarySearch (self, input_ID):
        
        low = 0
        high = self.record_size - 1
        found = False

        while not found and high >= low:

            self.middle = (low+high)//2
            #will update the fields in record dict automatically

            self.getRecord(self.middle)
            mid_id = self.record["ID"]
            
            if mid_id!="":
                if int(mid_id) == int(input_ID):
                    found = True
                    break
                elif int(mid_id) > int(input_ID):
                    high = self.middle - 1
                elif int(mid_id) < int(input_ID):
                    low = self.middle + 1

        if found:
            return True

        else:
            print("Could not find record with ID {input_ID}")
            return -1


    #open the database/also acting as my read data method
    def OpenDB(self, nameDB):
        if self.isOpen():
           print("You already have a database open.  Please close it first.")
        else:
           data_file = nameDB + ".data"
           config_file = nameDB + ".config"
        
           if not os.path.isfile(data_file):
              print(str(data_file)+" not found")
           else:
              if not os.path.isfile(config_file):
                 print(str(config_file)+" not found")
              else:
                 self.fileptr = open(data_file, "r+")
                 config_fileptr = open (config_file, "r")
                 self.num_records = int(config_fileptr.readline())
                 self.record_size = int(config_fileptr.readline())
                 config_fileptr.close();

    #check if a database is already open or not
    def isOpen(self):
        if self.fileptr == None:
            return False
        else:
            return True


    #close the database
    def CloseDB(self):
        if self.fileptr:
            self.fileptr.close()
            self.num_records = 0
            self.record_size = 0
            self.fileptr = None
            self.filestream = None
            print("Database closed!")
        else:
            print("You do not have any databases open to close them.")
