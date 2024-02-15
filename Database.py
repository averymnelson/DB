import csv
import os.path
from converter import converter


class DB:

    # default constructor
    def __init__(self):
        self.filestream = None
        self.numRecords = 0
        self.record_size = 75
        self.total_size = 0
        self.name = None
        self.isopen = False

    def isOpen(self):
        return self.isopen

    def write_record(self, data, output_file, record_size):
        with open(output_file, 'a') as file:
            formatted_data = ','.join(str(value) for value in data)
            file.write(formatted_data.ljust(record_size) + '\n')

    def write_blank(self, output_file):
        with open(output_file, 'a') as file:
            file.write('\n'.ljust(self.record_size))

    def readCSV(self, filename):
        self.name = filename
        with open(f"{filename}.csv", 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                self.write_record(row, f"{filename}.data", self.record_size)
                self.total_size += self.record_size
                self.write_blank(f"{filename}.data")
                self.total_size += self.record_size
                self.numRecords += 1

        with open(f"{filename}.config", 'w') as config_file:
            config_file.write(str(self.numRecords) + '\n')
            config_file.write(str(self.total_size) + '\n')
            config_file.close()

        self.isopen = True

    def read_record(self, recordnum):
        self.flag = False
        if 0 <= recordnum < self.numRecords:
            self.text_filename = f"{self.name}.data"
            with open(self.text_filename, 'r') as file:
                file.seek(0, 0)
                file.seek(recordnum * self.record_size)
                line = file.readline().rstrip('\n')
            self.flag = True
        else:
            print("Record number out of range.")
            return -1

        if self.flag:
            parts = line.split(',')
            if len(parts) >= 7:
                print(parts)
                p_id = parts[0]
                fname = parts[1]
                lname = parts[2]
                age = parts[3]
                t_num = parts[4]
                fare = parts[5]
                day_pur = parts[6]
                self.record = dict({"ID": p_id, "FIRST_NAME": fname, "LAST_NAME": lname, "AGE": age, "TICKET_NUM": t_num,"FARE": fare, "DAY_OF_PURCHASE": day_pur})
            else:
                print("empty")


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
            with open(f"{name}.config", 'r') as config_file:
                self.numRecords = int(config_file.readline().strip())
                self.recordSize = int(config_file.readline().strip())

            self.dataFileptr = open(f"{name}.data", 'r')

            self.name = name
            return True
        except Exception as e:
            print(f"Error opening database: {e}")
            return False

    def close_db(self):
        self.isopen = False
        if self.filestream:
            self.filestream.close()
            self.filestream = None
    
    def display_record(self):
        pass

    def create_report(self):
        pass

    def update_record(self, passengerid, fname, lname, age, ticketnum, fare, date):
        pass

    def delete_record(self, passengerid):
        pass

    def add_record(self, passengerid, fname, lname, age, ticketnum, fare, date):
        pass

    def binarySearch (self, input_ID):
        
        low = 0
        high = self.record_size - 1
        found = False

        while not found and high >= low:

            self.middle = (low+high)//2
            #will update the fields in record dict automatically

            self.read_record(self.middle)
            mid_id = self.record["ID"]
            
            if mid_id!="":
                if int(mid_id) == int(input_ID):
                    found = True
                    break
                elif int(mid_id) > int(input_ID):
                    high = self.middle - 1
                elif int(mid_id) < int(input_ID):
                    low = self.middle + 1

        if not found:
            print("Could not find record with ID {input_ID}")
            return -1
        
        return found


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
            title = input(
                "Enter the name of the database you'd like to create. It should be the name of the CSV file without the extension.\n")
            db.readCSV(title)
        elif choice == '2':
            name = input("Enter the name of the database to open: ")
            if db.open(name):
                print("Database open.")
            else:
                print("Failed to open database.")
        elif choice == '3':
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
            test = db.binarySearch(44)
            print(test)
        elif choice == '6':
            # Create report
            pass
        elif choice == '7':
            # Update record
            pass
        elif choice == '8':
            # Delete record
            pass
        elif choice == '9':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()
