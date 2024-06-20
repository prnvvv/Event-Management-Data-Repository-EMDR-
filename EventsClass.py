from mysqlConnector import Cursor
from mysql.connector import Error
import numpy as np
import pandas as pd

conn, cursor = Cursor()

class Event:

    def __init__(self, eventName = None, date = None, location = None):
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
        except Error as e:
            print(f"Error creating Event table: {e}")

    def AddValues(self):
        try:
            insertData = """
            INSERT INTO Event (EventName, Date, Location) VALUES (%s, %s, %s)
            """
            data = (self.eventName, self.date, self.location)
            cursor.execute(insertData, data)
            conn.commit()
        except Error as e:
            print(f"Error adding Event values: {e}")

    def ModifyValues(self, option):
        try:
            if option == 1:
                neventName = input("Enter the new Event Name : ")
                modifyData = "UPDATE Event SET EventName = %s WHERE EventName = %s"
                cursor.execute(modifyData, (neventName, self.eventName))
                self.eventName = neventName
                conn.commit()
            elif option == 2:
                neventDate = input("Enter the new Event Date (YYYY-MM-DD) : ")
                modifyData = "UPDATE Event SET Date = %s WHERE Date = %s"
                cursor.execute(modifyData, (neventDate, self.date))
                self.date = neventDate
                conn.commit()
            elif option == 3:
                nLocation = input("Enter the new Event Location : ")
                modifyData = "UPDATE Event SET Location = %s WHERE Location = %s"
                cursor.execute(modifyData, (nLocation, self.location))
                self.location = nLocation
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error modifying Event: {e}")

    def DeleteValues(self, option):
        try:
            if option == 1:
                deventName = input("Enter the Event Name : ")
                deleteData = "DELETE FROM Event WHERE EventName = %s"
                cursor.execute(deleteData, (deventName,))
                conn.commit()
            elif option == 2:
                deventDate = input("Enter the Event Date (YYYY-MM-DD) : ")
                deleteData = "DELETE FROM Event WHERE Date = %s"
                cursor.execute(deleteData, (deventDate,))
                conn.commit()
            elif option == 3:
                dLocation = input("Enter the Event Location : ")
                deleteData = "DELETE FROM Event WHERE Location = %s"
                cursor.execute(deleteData, (dLocation,))
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error deleting Event: {e}")
    
    def PrintData(self, option):
        try:
            if option == 1:
                cursor.execute("SELECT * FROM Event")
                rows = cursor.fetchall()

                tableArray = np.array(rows)
                print(pd.DataFrame(tableArray, columns=["EventID", "EventName", "Date", "Location"]))
            if option == 2:
                eventName = input("Enter the Event Name: ")
                query = "SELECT * FROM Event WHERE EventName = %s"
                cursor.execute(query, (eventName,))
                event = cursor.fetchone()

                if event:
                    tableArray = np.array([event])
                    print(pd.DataFrame(tableArray, columns=["EventID", "EventName", "Date", "Location"]))
                else:
                    print(f"No event found with name '{eventName}'")
            if option == 3:
                eventDate = input("Enter the Event Date (YYYY-MM-DD): ")
                query = "SELECT * FROM Event WHERE Date = %s"
                cursor.execute(query, (eventDate,))
                events = cursor.fetchall()

                if events:
                    tableArray = np.array(events)
                    print(pd.DataFrame(tableArray, columns=["EventID", "EventName", "Date", "Location"]))
                else:
                    print(f"No events found on '{eventDate}'")
            if option == 4:
                location = input("Enter the Event Location: ")
                query = "SELECT * FROM Event WHERE Location = %s"
                cursor.execute(query, (location,))
                events = cursor.fetchall()

                if events:
                    tableArray = np.array(events)
                    print(pd.DataFrame(tableArray, columns=["EventID", "EventName", "Date", "Location"]))
                else:
                    print(f"No events found at location '{location}'")
        except Error as e:
            print(f"Error while printing data: {e}")