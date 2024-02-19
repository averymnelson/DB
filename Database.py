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

    def overwrite_record(self, data, output_file, record_size, record_number):
        with open(output_file, 'r+') as file:
            seek_position = record_number * record_size
            file.seek(seek_position)
            current_position = file.tell()
            if current_position != seek_position:
                # Adjust seek position to the beginning of the next record
                file.seek(current_position + record_size)
            formatted_data = ','.join(str(value) for value in data)
            file.write(formatted_data.ljust(record_size) + '\n')

    def write_blank(self, output_file):
        with open(output_file, 'a') as file:
            file.write('\n'.ljust(self.record_size))
    
    def overwrite_blank(self, output_file, record_size, record_number):
        with open(output_file, 'r+') as file:
            seek_position = record_number * record_size
            file.seek(seek_position)
            current_position = file.tell()
            if current_position != seek_position:
                # Adjust seek position to the beginning of the next record
                file.seek(current_position + record_size)
            file.write('\n'.ljust(record_size))

    def delete_blank_record(self, record_number):
        with open(f"{self.name}.data", 'r+') as file:
            # Calculate the seek position based on the record number and record size
            seek_position = record_number * self.record_size
            file.seek(seek_position)
            
            # Overwrite the blank record with blank data
            file.write('\n' * self.record_size)
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
                line = line.strip()
            self.flag = True
        else:
            # print("Record number out of range.")
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
                self.record = {}


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

    def create_report(self):
        pass

    def display_record(self, passengerid):
        num, found_record = self.binarySearch(int(passengerid))
        print("Record found:", found_record)

    def update_record(self, passengerid, fname, lname, age, ticketnum, fare, date):
        # Find the record using binary search
        num, found_record = self.binarySearch(int(passengerid))

        # Check if the record was found
        if found_record:
            # Update the specific fields of the record in memory
            found_record[1] = fname
            found_record[2] = lname
            found_record[3] = age
            found_record[4] = ticketnum
            found_record[5] = fare
            found_record[6] = date
            
            # Write the updated record back to the file
            self.overwrite_record(found_record, f"{self.name}.data", self.record_size, num)
            print("Record updated:", found_record)
        else:
            print("Record not found.")

    def delete_record(self, passenger_id):
        # Find the record using binary search
        record_number, found_record = self.binarySearch(int(passenger_id))

        # Check if the record was found
        if found_record:
            with open(f"{self.name}.data", 'r+') as fp:
    # read an store all lines into list
                lines = fp.readlines()
                # move file pointer to the beginning of a file
                fp.seek(0)
                # truncate the file
                fp.truncate()

                # start writing lines
                # iterate line and line number
                for number, line in enumerate(lines):
                    # delete line number 5 and 8
                    # note: list index start from 0
                    if number not in [int(record_number), int(record_number+1)]:
                        fp.write(line)
                            
            print("Record deleted:", found_record)
            return True
        else:
            print("Record not found.")
            return False

    def add_record(self, passengerid, fname, lname, age, ticketnum, fare, date):
        closest_rec_num, found = self.binarySearch(int(passengerid))
        if found:
            print("Record with the same ID already exists.")
            return

        # Determine the position to insert the new record
        if closest_rec_num is not None:
            insert_pos = closest_rec_num - 1
        else:
            insert_pos = self.numRecords  # Insert at the end if no closest record found

        # Shift existing records down to make space for the new record
        self.overwrite_blank(f"{self.name}.data", self.record_size, insert_pos - 1)
        self.overwrite_blank(f"{self.name}.data", self.record_size, insert_pos - 1)

        # Write the new record
        new_rec = [passengerid, fname, lname, age, ticketnum, fare, date]
        self.overwrite_record(new_rec, f"{self.name}.data", self.record_size, insert_pos - 1)
        self.overwrite_blank(f"{self.name}.data", self.record_size, insert_pos - 1)

        print("Record added:", new_rec)

# search and display record
    def binarySearch(self, target):
        low = 0
        high = self.numRecords - 1
        closest_record_num = None

        while low <= high:
            mid = (low + high) // 2
            record_start_pos = mid * (self.record_size + 1)  # Add 1 to skip over the empty line
            with open(f"{self.name}.data", 'r') as file:
                file.seek(record_start_pos)
                line = file.readline().rstrip('\n')

                # Skip empty lines until a non-empty record is found
                while not line.strip() and record_start_pos >= 0:
                    record_start_pos -= self.record_size + 1  # Add 1 to skip over the empty line
                    file.seek(record_start_pos)
                    line = file.readline().rstrip('\n')

                if not line.strip():
                    # If all previous records are empty, search in the upper half
                    low = mid + 1
                    continue

                parts = line.split(',')
                if len(parts) >= 7 and int(parts[0]) == target:
                    return mid, parts
                elif int(parts[0]) < target:
                    low = mid + 1
                else:
                    high = mid - 1

                if closest_record_num is None or abs(int(parts[0]) - target) < abs(closest_record_num - target):
                                closest_record_num = mid

        print("Record not found.")
        return closest_record_num, None

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
        print("9) Add Record")
        print("10) Quit")
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
            name = input("Enter the ID number you're searching for: ")
            try:
                userint = int(name)
                num, located = db.binarySearch(userint)
                print("Record found:", located)
            except ValueError:
                print("Input not an integer.")
        elif choice == '6':
            # Create report
            pass
        elif choice == '7':
            locatedrec = None
            print("WARNING: the passenger ID number cannot be changed.\n")
            pid = input("Enter the Passenger ID number you'd like to update: ")
            try:
                userint = int(pid)
                num, locatedrec = db.binarySearch(userint)
            except ValueError:
                print("Input not an integer.")
            if locatedrec:
                fname = input("Enter the new first name: ")
                lname = input("Enter the new last name: ")
                age = input("Enter the new age: ")
                tnum = input("Enter the new ticket number: ")
                fare = input("Enter the new fare: ")
                date = input("Enter the new date of purchase: ")
                db.update_record(pid,fname,lname,age,tnum,fare,date)
        elif choice == '8':
            locatedrec = None
            pid = input("Enter the Passenger ID number you'd like to delete: ")
            try:
                userint = int(pid)
                num, locatedrec = db.binarySearch(userint)
            except ValueError:
                print("Input not an integer.")
            if locatedrec:
                db.delete_record(pid)
        elif choice == '9':
            print("You are adding a new record, assuming the ID you choose does not already have one.")
            pid = input("Enter the new Passenger ID: ")
            try:
                userint = int(pid)
                num, locatedrec = db.binarySearch(userint)
            except ValueError:
                print("Input not an integer.")
            if locatedrec is None:
                fname = input("Enter the new first name: ")
                lname = input("Enter the new last name: ")
                age = input("Enter the new age: ")
                tnum = input("Enter the new ticket number: ")
                fare = input("Enter the new fare: ")
                date = input("Enter the new date of purchase: ")
                db.add_record(pid,fname,lname,age,tnum,fare,date)
        elif choice == '10':
            if db.isOpen():
                db.close_db()
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()
