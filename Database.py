import csv
import os.path
from converter import converter

# ID, fname, lname, age, ticketnum, fare, purchased
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
        self.filestream = None
        self.numRecords = 0
        self.record_size = 75
        self.total_size = 0
        self.name = None
        self.data = None
        self.isopen = False
    
    def isOpen(self):
        return self.isopen
    
    def read_src(self, name):
        self.name = name
        conv = converter(name)
        self.data = conv.get_df()
        print(self.data)

    def write_record(self, data, output_file, record_size):
        with open(output_file, 'a') as file:
            formatted_data = ','.join(str(value) for value in data)
            file.write(formatted_data.ljust(record_size) + '\n')
    
    def write_blank(self,output_file):
        with open(output_file, 'a') as file:
            file.write('\n'.ljust(self.record_size))
    # def writerecord(recordnum, passengerid, fname, lname, age, ticketnum, fare, date):
    #     pass
        # writeRecord: a private helper method (it may be public if you need to call it from the main program)
        # parameter(s): recordNum, passengerid, fname, lname, age, ticketnum, fare, date
        # returns: int (-1 if the recordNum is invalid, 0 if it is valid and we overwrote an empty record, 1 if we overwrote a non-empty record
        # purpose: Using formatted writes, writes a fixed length record at the location indicated by recordNum.

    def readCSV(self, filename): 
        self.name = filename         
        with open(f"{filename}.csv", 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                self.write_record(row, f"{filename}.data", self.record_size)
                self.total_size += self.record_size
                self.write_blank(f"{filename}.data")                
                self.total_size += self.record_size
                self.numRecords+=1

        with open(f"{filename}.config", 'w') as config_file:
            config_file.write(str(self.numRecords) + '\n')
            config_file.write(str(self.total_size) + '\n')
            config_file.close()
    
        self.isopen = True

    def read_record(self, recordnum):
        self.flag = False
        p_id = fname = lname = age = t_num = fare = day_pur = "None"
        if recordnum >= 0 and recordnum < self.numRecords:
            self.text_filename = f"{self.name}.data"
            with open(self.text_filename, 'r') as file:
                file.seek(0,0)
                file.seek(recordnum*self.record_size)
                line= file.readline().rstrip('\n')
            self.flag = True
        else:
            print("Record number out of range.")
            return -1

        if self.flag:
            parts = line.split(',')
            if len(parts)>=7:
                print(parts)
                p_id = parts[0]
                fname = parts[1]
                lname = parts[2]
                age = parts[3]
                t_num = parts[4]
                fare = parts[5]
                day_pur= parts[6]
                self.record = dict(
                    {"PASSENGER_ID": p_id, "FIRST_NAME": fname, "LAST_NAME": lname, "AGE": age, "TICKET_NUM": t_num, "FARE": fare, "DAY_OF_PURCHASE":day_pur})
            else:
                print("empty")
            
            # p_id = self.data.loc[recordnum,'PASSENGER_ID']
            # fname = self.data.loc[recordnum,'FIRST_NAME']
            # lname = self.data.loc[recordnum,'LAST_NAME']
            # age = self.data.loc[recordnum,'AGE']
            # t_num = self.data.loc[recordnum,'TICKET_NUM']
            # fare = self.data.loc[recordnum,'FARE']
            # day_pur= self.data.loc[recordnum,'DATE_OF_PURCHASE']
            # self.record = dict(
            #     {"PASSENGER_ID": p_id, "FIRST_NAME": fname, "LAST_NAME": lname, "AGE": age, "TICKET_NUM": t_num, "FARE": fare, "DAY_OF_PURCHASE":day_pur})

        # parse
        # readRecord: a private helper method (it may be public if you need to call it from the main program)
        # parameter(s): recordNum, &passengerid, &fname, &lname, &age, &ticketnum, &fare, &date
        # returns: int (-1 if the recordNum is invalid, 0 if it is valid but is an empty record, 1 the read was successful)
        # purpose: if db is open and recordNum is valid, it seeks to the beginning of recordNum in the already opened file and reads the key, if the key is not _empty_, it reads the rest of the record and fills the parameters.

    def update_record(self, passengerid, fname, lname, age, ticketnum, fare, date):
        pass
    # parameter(s): passengerid, fname, lname, age, ticketnum, fare, date
    # returns: Boolean, true if record is updated, false otherwise
    # purpose: if db is open, it uses binarySearch to locate the record. It then uses writeRecord to overwrite it. NOTE: it assumes that the key (passengerid) will not be changed or binarySearch will break.

    def delete_record(self, passengerid):
        pass
        # parameter(s): passengerid
        # returns: Boolean, true if record is deleted, false otherwise
        # purpose: if db is open, it uses binarySearch to locate the record. It then uses writeRecord to overwrite it with default (empty) values. It sets the passengerid to _empty_.

    def add_record(self, passengerid, fname, lname, age, ticketnum, fare, date):
        pass
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

    def open(self, name):
        if self.isopen:
            print("Database already open. Please close it first.")
            return True
        try:
            # Open config file to read numRecords and recordSize
            with open(f"{name}.config", 'r') as config_file:
                self.numRecords = int(config_file.readline().strip())
                self.recordSize = int(config_file.readline().strip())

            # Open data file in read/write mode and set dataFileptr
            self.dataFileptr = open(f"{name}.data", 'r')

            # Update values in other instance variables
            # For example, you might want to do something like this:
            # self.some_other_instance_variable = some_value
            self.name = name
            return True  # Return True if successful
        except Exception as e:
            print(f"Error opening database: {e}")
            return False  # Return False if unsuccessful
        # parameter: name to use
        # returns: boolean of success
        # purpose:open config file to read numRecords and recordSize then closes it again. opens data file in read/write mode and sets dataFileptr to open file, updates values in other instance variables.

    # close the database
    def close_db(self):
        self.isopen = False
        if self.filestream:
            self.filestream.close()
            self.filestream = None

    # parameter(s): none
    # returns: nothing
    # purpose: resets instance variables, e.g., sets numRecords and recordSize to 0, closes the datafile, sets dataFileptr to NULL, etc.


def main():
    db = DB()
    while True:
        print("Menu of operations:")
        print("1) Create New Database")
        print("2) Open Database")
        print("3) Close Database")
        print("4) Read Record")
        print("5) Display Record")
        print("6) Create Report")
        print("7) Update Record")
        print("8) Delete Record")
        print("9) Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the name of the database you'd like to create. It should be the name of the CSV file without the extension.\n")
            db.readCSV(title)
        elif choice == '2':
            # Open database
            name = input("Enter the name of the database to open: ")
            if db.open(name):
                print("Database open.")
            else:
                print("Failed to open database.")
        elif choice == '3':
            # Close database
            if db.isOpen():
                db.close_db()
                print("Database closed.")
            else:
                print("No database is currently open.")
        elif choice == '4':
            name = input("Enter the record number you're searching for: ")
            try:
                userint = int(name)
                db.read_record(userint)
            except ValueError:
                print("Input not an integer.")
        elif choice == '5':
            # Display record
            pass  # Implement this option
        elif choice == '6':
            # Create report
            pass  # Implement this option
        elif choice == '7':
            # Update record
            pass  # Implement this option
        elif choice == '8':
            # Delete record
            pass  # Implement this option
        elif choice == '9':
            # Quit
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
