from mysqlConnector import Cursor  # Import the custom Cursor function to connect to the database
from mysql.connector import Error  # Import the Error class to handle MySQL errors
import numpy as np  # Import numpy for array manipulations
import pandas as pd  # Import pandas for data manipulation and display

# Establish connection to the database and get cursor object
conn, cursor = Cursor()

class Attendees:
    """
    Class to manage attendee-related operations in the database.
    """
    def __init__(self, attendeeName=None, email=None):
        """
        Initialize the Attendees object with optional attributes.
        """
        self.attendeeName = attendeeName
        self.email = email

    def CreateTable(self):
        """
        Create the Attendees table if it doesn't already exist.
        """
        try:
            attendeeTable = """
            CREATE TABLE IF NOT EXISTS Attendees(
            AttendeeID INT AUTO_INCREMENT PRIMARY KEY,
            AttendeeName VARCHAR(255) NOT NULL,
            AttendeeEmail VARCHAR(255) NOT NULL)
            """
            cursor.execute(attendeeTable)  # Execute the SQL command
            conn.commit()  # Commit the changes to the database
            print("Attendees table created successfully.")
        except Error as e:
            print(f"Error creating Attendees table: {e}")

    def AddValues(self, attendeeName, email):
        """
        Add a new attendee to the Attendees table.
        """
        try:
            insertData = """
            INSERT INTO Attendees (AttendeeName, AttendeeEmail) VALUES (%s, %s)  
            """
            data = (attendeeName, email)  # Data to be inserted
            cursor.execute(insertData, data)  # Execute the SQL command
            conn.commit()  # Commit the changes to the database
            print("Attendee added successfully.")
        except Error as e:
            print(f"Error adding Attendee values: {e}")

    def ModifyValues(self, option, newValue):
        """
        Modify an existing attendee in the Attendees table.
        """
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
            
            conn.commit()  # Commit the changes to the database
            print("Attendee modified successfully.")
        except Error as e:
            print(f"Error modifying Attendees: {e}")

    def DeleteValues(self, option, value):
        """
        Delete an attendee from the Attendees table based on a specified option.
        """
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
            
            cursor.execute(deleteData, (value,))  # Execute the SQL command
            conn.commit()  # Commit the changes to the database

            if cursor.rowcount > 0:
                print("Attendee deleted successfully.")
            else:
                print("No attendee found to delete.")
        except Error as e:
            print(f"Error deleting Attendees: {e}")

    def PrintData(self, option, value=None):
        """
        Print attendee data based on a specified option.
        """
        try:
            if option == 1:
                cursor.execute("SELECT * FROM Attendees")
                rows = cursor.fetchall()  # Fetch all rows from the query

                if rows:
                    tableArray = np.array(rows)  # Convert to numpy array
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))  # Display as DataFrame
                else:
                    print("No attendees found.")
            elif option == 2:
                query = "SELECT * FROM Attendees WHERE AttendeeName = %s"
                cursor.execute(query, (value,))
                attendee = cursor.fetchone()  # Fetch one row from the query

                if attendee:
                    tableArray = np.array([attendee])  # Convert to numpy array
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))  # Display as DataFrame
                else:
                    print(f"No attendee found with name '{value}'")
            elif option == 3:
                query = "SELECT * FROM Attendees WHERE AttendeeEmail = %s"
                cursor.execute(query, (value,))
                attendees = cursor.fetchall()  # Fetch all rows from the query

                if attendees:
                    tableArray = np.array(attendees)  # Convert to numpy array
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))  # Display as DataFrame
                else:
                    print(f"No attendees found with email '{value}'")
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error while printing data: {e}")

class Registration:
    """
    Class to manage registration-related operations in the database.
    """
    def __init__(self, eventID=None, attendeeID=None, eventName=None, attendeeName=None):
        """
        Initialize the Registration object with optional attributes.
        """
        self.eventID = eventID
        self.attendeeID = attendeeID
        self.eventName = eventName
        self.attendeeName = attendeeName

    @classmethod
    def CreateTable(cls):
        """
        Create the Registration table if it doesn't already exist.
        """
        try:
            registrationTable = """
            CREATE TABLE IF NOT EXISTS Registration(
            RegistrationID INT AUTO_INCREMENT PRIMARY KEY,
            EventID INT,
            AttendeeID INT,
            EventName VARCHAR(255),
            AttendeeName VARCHAR(255),
            FOREIGN KEY (EventID) REFERENCES Event(EventID) ON DELETE CASCADE,
            FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE)
            """
            cursor.execute(registrationTable)  # Execute the SQL command
            conn.commit()  # Commit the changes to the database
        except Error as e:
            print(f"Error creating Registration table: {e}")

    def AddValues(self):
        """
        Add a new registration to the Registration table.
        """
        try:
            insertData = """
            INSERT INTO Registration (EventID, AttendeeID, EventName, AttendeeName) VALUES (%s, %s, %s, %s)
            """
            data = (self.eventID, self.attendeeID, self.eventName, self.attendeeName)
            cursor.execute(insertData, data)  # Execute the SQL command
            conn.commit()  # Commit the changes to the database
        except Error as e:
            print(f"Error adding Registration values: {e}")

    def ModifyValues(self, option):
        """
        Modify an existing registration in the Registration table.
        """
        try:
            registrationID = input("Enter the Registration ID to modify: ")

            if option == 1:
                newEventID = input("Enter the new Event ID: ")
                modifyData = "UPDATE Registration SET EventID = %s WHERE RegistrationID = %s"
                cursor.execute(modifyData, (newEventID, registrationID))
                conn.commit()
            elif option == 2:
                newAttendeeID = input("Enter the new Attendee ID: ")
                modifyData = "UPDATE Registration SET AttendeeID = %s WHERE RegistrationID = %s"
                cursor.execute(modifyData, (newAttendeeID, registrationID))
                conn.commit()
            elif option == 3:
                newEventName = input("Enter the new Event Name: ")
                modifyData = "UPDATE Registration SET EventName = %s WHERE RegistrationID = %s"
                cursor.execute(modifyData, (newEventName, registrationID))
                conn.commit()
            elif option == 4:
                newAttendeeName = input("Enter the new Attendee Name: ")
                modifyData = "UPDATE Registration SET AttendeeName = %s WHERE RegistrationID = %s"
                cursor.execute(modifyData, (newAttendeeName, registrationID))
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error modifying Registration: {e}")

    def DeleteValues(self):
        """
        Delete a registration from the Registration table.
        """
        try:
            registrationID = input("Enter the Registration ID to delete: ")
            deleteData = "DELETE FROM Registration WHERE RegistrationID = %s"
            cursor.execute(deleteData, (registrationID,))
            conn.commit()
        except Error as e:
            print(f"Error deleting Registration: {e}")

    def PrintData(self, option):
        """
        Print registration data based on a specified option.
        """
        try:
            if option == 1:
                cursor.execute("SELECT * FROM Registration")
                rows = cursor.fetchall()  # Fetch all rows from the query

                if rows:
                    tableArray = np.array(rows)  # Convert to numpy array
                    print(pd.DataFrame(tableArray, columns=["RegistrationID", "EventID", "AttendeeID", "EventName", "AttendeeName"]))  # Display as DataFrame
                else:
                    print("No registrations found.")
            elif option == 2:
                registrationID = input("Enter the Registration ID: ")
                query = "SELECT * FROM Registration WHERE RegistrationID = %s"
                cursor.execute(query, (registrationID,))
                registration = cursor.fetchone()  # Fetch one row from the query

                if registration:
                    tableArray = np.array([registration])  # Convert to numpy array
                    print(pd.DataFrame(tableArray, columns=["RegistrationID", "EventID", "AttendeeID", "EventName", "AttendeeName"]))  # Display as DataFrame
                else:
                    print(f"No registration found with ID '{registrationID}'")
            elif option == 3:
                eventID = input("Enter the Event ID: ")
                query = "SELECT * FROM Registration WHERE EventID = %s"
                cursor.execute(query, (eventID,))
                registrations = cursor.fetchall()  # Fetch all rows from the query

                if registrations:
                    tableArray = np.array(registrations)  # Convert to numpy array
                    print(pd.DataFrame(tableArray, columns=["RegistrationID", "EventID", "AttendeeID", "EventName", "AttendeeName"]))  # Display as DataFrame
                else:
                    print(f"No registrations found for event ID '{eventID}'")
            elif option == 4:
                attendeeID = input("Enter the Attendee ID: ")
                query = "SELECT * FROM Registration WHERE AttendeeID = %s"
                cursor.execute(query, (attendeeID,))
                registrations = cursor.fetchall()  # Fetch all rows from the query

                if registrations:
                    tableArray = np.array(registrations)  # Convert to numpy array
                    print(pd.DataFrame(tableArray, columns=["RegistrationID", "EventID", "AttendeeID", "EventName", "AttendeeName"]))  # Display as DataFrame
                else:
                    print(f"No registrations found for attendee ID '{attendeeID}'")
        except Error as e:
            print(f"Error while printing data: {e}")

# Example usage:
if __name__ == "__main__":
    attendee = Attendees()  # Create an instance of Attendees class
    registration = Registration()  # Create an instance of Registration class

    while True:
        print()
        print
