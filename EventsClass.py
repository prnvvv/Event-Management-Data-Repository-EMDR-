from mysqlConnector import Cursor  # Import the custom Cursor function
from mysql.connector import Error  # Import the Error class from mysql.connector
import numpy as np  # Import numpy for numerical operations
import pandas as pd  # Import pandas for data manipulation

# Establish connection to the database and get cursor object
conn, cursor = Cursor()

class Event:
    """
    Class to manage event-related operations in the database.
    """
    def __init__(self, eventName=None, date=None, location=None):
        """
        Initialize the Event object with optional attributes.
        """
        self.eventName = eventName
        self.date = date
        self.location = location

    def CreateTable(self):
        """
        Create the Event table if it doesn't already exist.
        """
        try:
            eventTable = """
            CREATE TABLE IF NOT EXISTS Event(
            EventID INT AUTO_INCREMENT PRIMARY KEY,
            EventName VARCHAR(255) NOT NULL,
            Date DATE NOT NULL,
            Location VARCHAR(255) NOT NULL)
            """
            cursor.execute(eventTable)
            conn.commit()
            print("Event table created successfully.")
        except Error as e:
            print(f"Error creating Event table: {e}")

    def AddValues(self, eventName, eventDate, eventLocation):
        """
        Add a new event to the Event table.
        """
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
        """
        Modify an existing event in the Event table.
        """
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
        """
        Delete an event from the Event table based on a specified option.
        """
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
        """
        Print event data based on a specified option.
        """
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