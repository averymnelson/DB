import csv
import os


class DB:
    def __init__(self):
        self.recordSize = 0
        self.numRecords = 0
        self.dataFileptr = None

    def open(self, name):
        # Open config file to read numRecords and recordSize
        try:
            with open(f"{name}.config", 'r') as config_file:
                config_data = config_file.readlines()
                self.numRecords = int(config_data[0].strip())
                self.recordSize = int(config_data[1].strip())
        except FileNotFoundError:
            print("Config file not found.")
            return False

        # Open data file in read/write mode
        try:
            self.dataFileptr = open(f"{name}.data", 'r+')
        except FileNotFoundError:
            print("Data file not found.")
            return False

        return True

    def close(self):
        # Close the data file
        if self.dataFileptr:
            self.dataFileptr.close()
            self.dataFileptr = None
            self.numRecords = 0
            self.recordSize = 0

    def isOpen(self):
        return self.dataFileptr is not None

    def readRecord(self, recordNum, passengerId, fname, lname, age, ticketNum, fare, date):
        if not self.isOpen():
            print("Database is not open.")
            return -1

        if recordNum < 0 or recordNum >= self.numRecords:
            print("Invalid record number.")
            return -1

        self.dataFileptr.seek(recordNum * self.recordSize)
        record_data = self.dataFileptr.read(self.recordSize)

        # Assuming fields are comma-separated in the record
        fields = record_data.strip().split(',')
        passengerId.value = fields[0]
        fname.value = fields[1]
        lname.value = fields[2]
        age.value = fields[3]
        ticketNum.value = fields[4]
        fare.value = fields[5]
        date.value = fields[6]

        return 1

    def writeRecord(self, recordNum, passengerId, fname, lname, age, ticketNum, fare, date):
        if not self.isOpen():
            print("Database is not open.")
            return -1

        if recordNum < 0 or recordNum >= self.numRecords:
            print("Invalid record number.")
            return -1

        self.dataFileptr.seek(recordNum * self.recordSize)
        record_data = f"{passengerId},{fname},{lname},{age},{ticketNum},{fare},{date}".ljust(self.recordSize)
        self.dataFileptr.write(record_data)

        return 1

    def binarySearch(self, passengerId, recordNum, fname, lname, age, ticketNum, fare, date):
        # Implement binary search to locate the record based on passengerId
        pass

    def updateRecord(self, passengerId, fname, lname, age, ticketNum, fare, date):
        # Implement updateRecord method
        pass

    def deleteRecord(self, passengerId):
        # Implement deleteRecord method
        pass

    def addRecord(self, passengerId, fname, lname, age, ticketNum, fare, date):
        # Implement addRecord method
        pass


def display_menu():
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


def main():
    db = DB()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Create new database
            pass  # Implement this option
        elif choice == '2':
            # Open database
            name = input("Enter the name of the database to open: ")
            if db.isOpen():
                print("Another database is already open. Please close it first.")
            else:
                if db.open(name):
                    print("Database opened successfully.")
                else:
                    print("Failed to open database.")
        elif choice == '3':
            # Close database
            if db.isOpen():
                db.close()
                print("Database closed.")
            else:
                print("No database is currently open.")
        elif choice == '4':
            # Read record
            pass  # Implement this option
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
