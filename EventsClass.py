from mysqlConnector import Cursor
from mysql.connector import Error
import numpy as np
import pandas as pd

conn, cursor = Cursor()

class Event:

    def __init__(self, eventName=None, date=None, location=None):
        self.eventName = eventName
        self.date = date
        self.location = location

    def CreateTable(self):
        try:
            eventTable = """
            CREATE TABLE IF NOT EXISTS Event(
            EventID INT AUTO_INCREMENT PRIMARY KEY,
            EventName VARCHAR(255) NOT NULL,
            Date DATE NOT NULL,
            Location VARCHAR(255) NOT NULL)"""
            cursor.execute(eventTable)
            conn.commit()
            print("Event table created successfully.")
        except Error as e:
            print(f"Error creating Event table: {e}")

    def AddValues(self, eventName, eventDate, eventLocation):
        try:
            insertData = """
            INSERT INTO Event (EventName, Date, Location) VALUES (%s, %s, %s)
            """
            data = (eventName, eventDate, eventLocation)
            cursor.execute(insertData, data)
            conn.commit()
            print("Event added successfully.")
        except Error as e:
            print(f"Error adding Event values: {e}")

    def ModifyValues(self, option, newValue):
        try:
            if option == 1:
                modifyData = "UPDATE Event SET EventName = %s WHERE EventName = %s"
                cursor.execute(modifyData, (newValue, self.eventName))
                self.eventName = newValue
            elif option == 2:
                modifyData = "UPDATE Event SET Date = %s WHERE EventName = %s"
                cursor.execute(modifyData, (newValue, self.eventName))
                self.date = newValue
            elif option == 3:
                modifyData = "UPDATE Event SET Location = %s WHERE EventName = %s"
                cursor.execute(modifyData, (newValue, self.eventName))
                self.location = newValue
            else:
                print("Invalid Option")
            
            conn.commit()
            print("Event modified successfully.")
        except Error as e:
            print(f"Error modifying Event: {e}")

    def DeleteValues(self, option, value):
        try:
            if option == 1:
                deleteData = "DELETE FROM Event WHERE EventName = %s"
            elif option == 2:
                deleteData = "DELETE FROM Event WHERE Date = %s"
            elif option == 3:
                deleteData = "DELETE FROM Event WHERE Location = %s"
            else:
                print("Invalid Option")
                return
            
            cursor.execute(deleteData, (value,))
            conn.commit()

            if cursor.rowcount > 0:
                print("Event deleted successfully.")
            else:
                print("No event found to delete.")
        except Error as e:
            print(f"Error deleting Event: {e}")
    
    def PrintData(self, option, value=None):
        try:
            if option == 1:
                cursor.execute("SELECT * FROM Event")
                rows = cursor.fetchall()

                if rows:
                    tableArray = np.array(rows)
                    print(pd.DataFrame(tableArray, columns=["EventID", "EventName", "Date", "Location"]))
                else:
                    print("No events found.")
            elif option == 2:
                query = "SELECT * FROM Event WHERE EventName = %s"
                cursor.execute(query, (value,))
                event = cursor.fetchone()

                if event:
                    tableArray = np.array([event])
                    print(pd.DataFrame(tableArray, columns=["EventID", "EventName", "Date", "Location"]))
                else:
                    print(f"No event found with name '{value}'")
            elif option == 3:
                query = "SELECT * FROM Event WHERE Date = %s"
                cursor.execute(query, (value,))
                events = cursor.fetchall()

                if events:
                    tableArray = np.array(events)
                    print(pd.DataFrame(tableArray, columns=["EventID", "EventName", "Date", "Location"]))
                else:
                    print(f"No events found on '{value}'")
            elif option == 4:
                query = "SELECT * FROM Event WHERE Location = %s"
                cursor.execute(query, (value,))
                events = cursor.fetchall()

                if events:
                    tableArray = np.array(events)
                    print(pd.DataFrame(tableArray, columns=["EventID", "EventName", "Date", "Location"]))
                else:
                    print(f"No events found at location '{value}'")
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error while printing data: {e}")

# Example usage:
if __name__ == "__main__":
    event = Event()

    while True:
        print()
        print("MENU")
        print("1. Create Event Table")
        print("2. Add Event")
        print("3. Modify Event")
        print("4. Delete Event")
        print("5. Print Events")
        print("6. Exit")
        print()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            event.CreateTable()
        elif choice == 2:
            eventName = input("Enter Event Name: ")
            eventDate = input("Enter Event Date (YYYY-MM-DD): ")
            eventLocation = input("Enter Event Location: ")
            event.AddValues(eventName, eventDate, eventLocation)
        elif choice == 3:
            print("MODIFY MENU")
            print("1. Update Event Name")
            print("2. Update Event Date")
            print("3. Update Event Location")
            modifyOption = int(input("Enter your option: "))
            if modifyOption in [1, 2, 3]:
                newValue = input("Enter new value: ")
                event.ModifyValues(modifyOption, newValue)
            else:
                print("Invalid option.")
        elif choice == 4:
            print("DELETE MENU")
            print("1. Delete by Event Name")
            print("2. Delete by Event Date")
            print("3. Delete by Event Location")
            deleteOption = int(input("Enter your option: "))
            if deleteOption in [1, 2, 3]:
                value = input("Enter value to delete: ")
                event.DeleteValues(deleteOption, value)
            else:
                print("Invalid option.")
        elif choice == 5:
            print("PRINT DATA MENU")
            print("1. Print all events")
            print("2. Print event by name")
            print("3. Print events by date")
            print("4. Print events by location")
            printOption = int(input("Enter your option: "))
            if printOption == 1:
                event.PrintData(1)
            elif printOption == 2:
                eventName = input("Enter Event Name: ")
                event.PrintData(2, eventName)
            elif printOption == 3:
                eventDate = input("Enter Event Date (YYYY-MM-DD): ")
                event.PrintData(3, eventDate)
            elif printOption == 4:
                eventLocation = input("Enter Event Location: ")
                event.PrintData(4, eventLocation)
            else:
                print("Invalid option.")
        elif choice == 6:
            print("Exiting Event Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
