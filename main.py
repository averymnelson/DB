import os.path
from Database import DB

db = DB()

def main():
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
            name = name.strip()
            try:
                userint = int(name)
                db.read_record(userint)
            except ValueError:
                print("Input not an integer.")
        elif choice == '5':
            name = input("Enter the ID number you're searching for: ")
            name = name.strip()
            print("User input:", name) 
            try:
                userint = int(name)
                num, located = db.binarySearch(userint)
                print("Record found:", located)
            except ValueError:
                print("Input not an integer.")
        elif choice == '6':
            db.create_report()
        elif choice == '7':
            locatedrec = None
            print("WARNING: the passenger ID number cannot be changed.\n")
            pid = input("Enter the Passenger ID number you'd like to update: ")
            pid = pid.strip()
            try:
                userint = int(pid)
                num, locatedrec = db.binarySearch(userint)
            except ValueError:
                print("Input not an integer.")
            if locatedrec:
                fname = input("Enter the new first name: ")
                fname = fname.strip()
                lname = input("Enter the new last name: ")
                lname = lname.strip()
                age = input("Enter the new age: ")
                age = age.strip()
                tnum = input("Enter the new ticket number: ")
                tnum = tnum.strip()
                fare = input("Enter the new fare: ")
                fare = fare.strip()
                date = input("Enter the new date of purchase: ")
                date = date.strip()
                db.update_record(pid,fname,lname,age,tnum,fare,date)
                for file in [f"{db.getName()}.csv", f"{db.getName()}.config"]:
                    if os.path.exists(file):
                        os.remove(file)
                db.convert_data_to_csv()
                title = db.getName()
                filename2 = f"{title}.data"
                db.close_db()
                if os.path.exists(filename2):
                        os.remove(filename2)
                db.readCSV(title)   
        elif choice == '8':
            locatedrec = None
            pid = input("Enter the Passenger ID number you'd like to delete: ")
            pid = pid.strip()
            try:
                userint = int(pid)
                num, locatedrec = db.binarySearch(userint)
            except ValueError:
                print("Input not an integer.")
            if locatedrec:
                db.delete_record(pid)
                for file in [f"{db.getName()}.csv", f"{db.getName()}.config"]:
                    if os.path.exists(file):
                        os.remove(file)
                db.convert_data_to_csv()
                title = db.getName()
                filename2 = f"{title}.data"
                db.close_db()
                if os.path.exists(filename2):
                        os.remove(filename2)
                db.readCSV(title)   
        elif choice == '9':
            print("You are adding a new record, assuming the ID you choose does not already have one.")
            pid = input("Enter the new Passenger ID: ")
            pid = pid.strip()
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
                for file in [f"{db.getName()}.csv", f"{db.getName()}.config"]:
                    if os.path.exists(file):
                        os.remove(file)
                db.add_record(pid,fname,lname,age,tnum,fare,date)
                title = db.getName()
                filename2 = f"{title}.data"
                db.close_db()
                if os.path.exists(filename2):
                        os.remove(filename2)
                db.readCSV(title)        
            else:
                print("There appears to already be a record with this ID.")    
        elif choice == '10':
            if db.isOpen():
                db.close_db()
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please try again.")

main()
