import os.path
from Database import DB

sample = DB()

# Menu Function
def menu():
    print("Welcome to the Database")
    print()

    done = False
    while done == False:
        choice = input("""
        1) Create new database
        2) Open database
        3) Close database
        4) Read record
        5) Display record
        6) Update record
        7) Create report
        8) Add record
        9) Delete record
        10) Quit

        Please enter your choice: """)

        choice = int(choice)
        if choice == 1:
           #infinite loop till the user types a valid csv file
           while True:
              created_db_file = input("What is the name of the file? ")
              if not os.path.isfile(created_db_file + str(".csv")):
                 print(str(created_db_file)+".csv not found")
              else:
                 sample.createDB(created_db_file)
                 break

        elif choice == 2:
           #Checks to see if a database is already open. If not, prompts the user with the available databases to open.
           if sample.isOpen():
              print("A database is already open. Please close that first.")
           else:
              selected_database = input("Type the database you want to open: ")
              sample.OpenDB(selected_database)

        elif choice == 3:
           #Closes the database
           sample.CloseDB()

        elif choice == 4:
           #Get specific record by seeking to that place. If no database is open, print error message.
           if sample.isOpen():
              number = input("What record do you want to read? ")
              sample.getRecord(int(number))
              print("Record "+ str(number) + ", ID: "+sample.record["ID"]+"\t first_name: "+sample.record["first_name"]+"\t last_name: "+sample.record["last_name"]+"\t age: "+str(sample.record["age"])+"\t ticket_num: "+sample.record["ticket_num"]+"\t fare: "+sample.record["fare"]+"\t date_of_purchase: "+sample.record["date_of_purchase"])
           else:
              print("Database is closed. Open to use.")

        elif choice == 5:
           print("Displaying record")
        elif choice == 6:
           print("Updating record")
        elif choice == 7:
           print("Creating record")
        elif choice == 8:
              print("Adding record")
        elif choice == 9:
           print("Deleting record")
        elif choice == 10:
           if sample.isOpen():
              print ("Please close the database first.")
           else:
              print("Quitting")
              done = True
        else:
           print("Invalid option")


# Calling the Menu Function
menu()
