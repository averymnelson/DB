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
        self.fileptr = None

    def isOpen(self):
        if self.fileptr == None:
            return False
        else:
            return True

    def getName(self):
        return self.name
    
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

            self.fileptr = open(f"{name}.data", 'r')

            self.name = name
            return True
        except Exception as e:
            print(f"Error opening database: {e}")
            return False

    def close_db(self):
        self.isopen = False
        if self.fileptr:
            self.fileptr.close()
            self.num_records = 0
            self.record_size = 0
            self.fileptr = None
            self.filestream = None
            print("Database closed.")

    def create_report(self):
        filename = f"{self.name}.data"
        with open(filename, 'r') as file:
            for _ in range(20):
                line = file.readline().rstrip('\n')
                if line.strip():  # Check if the line is not empty
                    parts = line.split(',')
                    print("Passenger ID:", parts[0])
                    print("First Name:", parts[1])
                    print("Last Name:", parts[2])
                    print("Age:", parts[3])
                    print("Ticket Number:", parts[4])
                    print("Fare:", parts[5])
                    print("Date of Purchase:", parts[6])
                    print()

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
        new_record = [passengerid, fname, lname, age, ticketnum, fare, date]  # Create a list of record fields
        filename = f"{self.name}.data"

        with open(filename, 'a') as file:
            formatted_record = ','.join(map(str, new_record))  # Convert each field to string and join them with commas
            file.write(formatted_record + '\n')  # Write the formatted record to the file

        self.numRecords += 1
        self.convert_data_to_csv()

    def convert_data_to_csv(self):
        unique_values = set()  # Set to store unique values
        csv_filename = f"{self.name}.csv"  # Assuming the CSV file has the same name as the database
        
        # Read data from .data file and add unique non-empty records to CSV
        with open(f"{self.name}.data", 'r') as data_file:
            with open(csv_filename, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                
                # Iterate over each line in the .data file
                for line in data_file:
                    # Strip leading/trailing whitespace and check if the line is empty
                    line = line.strip()
                    if line:
                        # Split the record into fields (assuming comma-separated)
                        fields = line.split(',')
                        
                        # Check if the first field (or any other unique identifier) is already in the set
                        if fields[0] not in unique_values:
                            # Write the fields to the CSV file
                            csv_writer.writerow(fields)
                            
                            # Add the value to the set to mark it as encountered
                            unique_values.add(fields[0])

        # Sort the CSV file based on the first column (assuming Passenger ID)
        self.sort_csv(csv_filename)

    def sort_csv(self, csv_filename):
        # Read the CSV file into a list of rows
        with open(csv_filename, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)

        # Sort the rows based on the first column (Passenger ID)
        sorted_rows = sorted(rows, key=lambda x: int(x[0]))

        # Write the sorted rows back to the CSV file
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(sorted_rows)


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
                line = line.strip()

                # Skip empty lines until a non-empty record is found
                while not line.strip() and record_start_pos >= 0:
                    record_start_pos -= self.record_size + 1  # Add 1 to skip over the empty line
                    file.seek(record_start_pos)
                    line = file.readline().rstrip('\n')
                    line = line.strip()

                if not line.strip():
                    # If all previous records are empty, search in the upper half
                    low = mid + 1
                    continue

                parts = line.split(',')
                # print("Debug - parts:", parts) 
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
