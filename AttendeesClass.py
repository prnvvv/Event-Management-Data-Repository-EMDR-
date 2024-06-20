from mysqlConnector import Cursor
from mysql.connector import Error
import numpy as np
import pandas as pd

conn, cursor = Cursor()

class Attendees:

    def __init__(self, attendeeName=None, email=None):
        self.attendeeName = attendeeName
        self.email = email

    def CreateTable(self):
        try:
            attendeeTable = """
            CREATE TABLE IF NOT EXISTS Attendees(
            AttendeeID INT AUTO_INCREMENT PRIMARY KEY,
            AttendeeName VARCHAR(255) NOT NULL,
            AttendeeEmail VARCHAR(255) NOT NULL)"""
            cursor.execute(attendeeTable)
            conn.commit()
            print("Attendees table created successfully.")
        except Error as e:
            print(f"Error creating Attendees table: {e}")

    def AddValues(self, attendeeName, email):
        try:
            insertData = """
            INSERT INTO Attendees (AttendeeName, AttendeeEmail) VALUES (%s, %s)  
            """
            data = (attendeeName, email)
            cursor.execute(insertData, data)
            conn.commit()
            print("Attendee added successfully.")
        except Error as e:
            print(f"Error adding Attendee values: {e}")

    def ModifyValues(self, option, newValue):
        try:
            if option == 1:
                nattendeeName = input("Enter the new Attendee Name : ")
                modifyData = "UPDATE Attendees SET AttendeeName = %s WHERE AttendeeName = %s"
                cursor.execute(modifyData, (nattendeeName, self.attendeeName))
                self.attendeeName = nattendeeName
            elif option == 2:
                nattendeeEmail = input("Enter the new Attendee Email : ")
                modifyData = "UPDATE Attendees SET AttendeeEmail = %s WHERE AttendeeEmail = %s"
                cursor.execute(modifyData, (nattendeeEmail, self.email))
                self.email = nattendeeEmail
            else:
                print("Invalid Option")
            
            conn.commit()
            print("Attendee modified successfully.")
        except Error as e:
            print(f"Error modifying Attendees: {e}")

    def DeleteValues(self, option, value):
        try:
            if option == 1:
                dattendeeName = input("Enter the Attendee Name : ")
                deleteData = "DELETE FROM Attendees WHERE AttendeeName = %s"
            elif option == 2:
                demail = input("Enter the Attendee Email : ")
                deleteData = "DELETE FROM Attendees WHERE AttendeeEmail = %s"
            else:
                print("Invalid Option")
                return
            
            cursor.execute(deleteData, (value,))
            conn.commit()

            if cursor.rowcount > 0:
                print("Attendee deleted successfully.")
            else:
                print("No attendee found to delete.")
        except Error as e:
            print(f"Error deleting Attendees: {e}")

    def PrintData(self, option, value=None):
        try:
            if option == 1:
                cursor.execute("SELECT * FROM Attendees")
                rows = cursor.fetchall()

                if rows:
                    tableArray = np.array(rows)
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))
                else:
                    print("No attendees found.")
            elif option == 2:
                query = "SELECT * FROM Attendees WHERE AttendeeName = %s"
                cursor.execute(query, (value,))
                attendee = cursor.fetchone()

                if attendee:
                    tableArray = np.array([attendee])
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))
                else:
                    print(f"No attendee found with name '{value}'")
            elif option == 3:
                query = "SELECT * FROM Attendees WHERE AttendeeEmail = %s"
                cursor.execute(query, (value,))
                attendees = cursor.fetchall()

                if attendees:
                    tableArray = np.array(attendees)
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))
                else:
                    print(f"No attendees found with email '{value}'")
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error while printing data: {e}")

# Example usage:
if __name__ == "__main__":
    attendee = Attendees()

    while True:
        print()
        print("MENU")
        print("1. Create Attendees Table")
        print("2. Add Attendee")
        print("3. Modify Attendee")
        print("4. Delete Attendee")
        print("5. Print Attendees")
        print("6. Exit")
        print()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            attendee.CreateTable()
        elif choice == 2:
            attendeeName = input("Enter Attendee Name: ")
            email = input("Enter Attendee Email: ")
            attendee.AddValues(attendeeName, email)
        elif choice == 3:
            print("MODIFY MENU")
            print("1. Update Attendee Name")
            print("2. Update Attendee Email")
            modifyOption = int(input("Enter your option: "))
            if modifyOption in [1, 2]:
                newValue = input("Enter new value: ")
                attendee.ModifyValues(modifyOption, newValue)
            else:
                print("Invalid option.")
        elif choice == 4:
            print("DELETE MENU")
            print("1. Delete by Attendee Name")
            print("2. Delete by Attendee Email")
            deleteOption = int(input("Enter your option: "))
            if deleteOption in [1, 2]:
                value = input("Enter value to delete: ")
                attendee.DeleteValues(deleteOption, value)
            else:
                print("Invalid option.")
        elif choice == 5:
            print("PRINT DATA MENU")
            print("1. Print all attendees")
            print("2. Print attendee by name")
            print("3. Print attendees by email")
            printOption = int(input("Enter your option: "))
            if printOption == 1:
                attendee.PrintData(1)
            elif printOption == 2:
                attendeeName = input("Enter Attendee Name: ")
                attendee.PrintData(2, attendeeName)
            elif printOption == 3:
                email = input("Enter Attendee Email: ")
                attendee.PrintData(3, email)
            else:
                print("Invalid option.")
        elif choice == 6:
            print("Exiting Attendee Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
