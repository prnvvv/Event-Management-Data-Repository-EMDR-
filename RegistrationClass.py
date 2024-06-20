from mysqlConnector import Cursor
from mysql.connector import Error
import numpy as np
import pandas as pd

conn, cursor = Cursor()

class Registration:

    def CreateTable(self):
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
            cursor.execute(registrationTable)
            conn.commit()
        except Error as e:
            print(f"Error creating Registration table: {e}")

    def AddValues(self, eventID, attendeeID, eventName, attendeeName):
        try:
            insertData = """
            INSERT INTO Registration (EventID, AttendeeID, EventName, AttendeeName) VALUES (%s, %s, %s, %s)
            """
            data = (eventID, attendeeID, eventName, attendeeName)
            cursor.execute(insertData, data)
            conn.commit()
        except Error as e:
            print(f"Error adding Registration values: {e}")

    def ModifyValues(self, option):
        try:
            if option == 1:
                registrationID = input("Enter the Registration ID to modify: ")
                newEventID = input("Enter the new Event ID: ")
                modifyData = "UPDATE Registration SET EventID = %s WHERE RegistrationID = %s"
                cursor.execute(modifyData, (newEventID, registrationID))
                conn.commit()
            elif option == 2:
                registrationID = input("Enter the Registration ID to modify: ")
                newAttendeeID = input("Enter the new Attendee ID: ")
                modifyData = "UPDATE Registration SET AttendeeID = %s WHERE RegistrationID = %s"
                cursor.execute(modifyData, (newAttendeeID, registrationID))
                conn.commit()
            elif option == 3:
                registrationID = input("Enter the Registration ID to modify: ")
                newEventName = input("Enter the new Event Name: ")
                modifyData = "UPDATE Registration SET EventName = %s WHERE RegistrationID = %s"
                cursor.execute(modifyData, (newEventName, registrationID))
                conn.commit()
            elif option == 4:
                registrationID = input("Enter the Registration ID to modify: ")
                newAttendeeName = input("Enter the new Attendee Name: ")
                modifyData = "UPDATE Registration SET AttendeeName = %s WHERE RegistrationID = %s"
                cursor.execute(modifyData, (newAttendeeName, registrationID))
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error modifying Registration: {e}")

    def DeleteValues(self, registrationID):
        try:
            deleteData = "DELETE FROM Registration WHERE RegistrationID = %s"
            cursor.execute(deleteData, (registrationID,))
            conn.commit()
        except Error as e:
            print(f"Error deleting Registration: {e}")

    def PrintData(self, option):
        try:
            if option == 1:
                cursor.execute("SELECT * FROM Registration")
                rows = cursor.fetchall()

                tableArray = np.array(rows)
                print(pd.DataFrame(tableArray, columns=["RegistrationID", "EventID", "AttendeeID", "EventName", "AttendeeName"]))
            if option == 2:
                registrationID = input("Enter the Registration ID: ")
                query = "SELECT * FROM Registration WHERE RegistrationID = %s"
                cursor.execute(query, (registrationID,))
                registration = cursor.fetchone()

                if registration:
                    tableArray = np.array([registration])
                    print(pd.DataFrame(tableArray, columns=["RegistrationID", "EventID", "AttendeeID", "EventName", "AttendeeName"]))
                else:
                    print(f"No registration found with ID '{registrationID}'")
            if option == 3:
                eventID = input("Enter the Event ID: ")
                query = "SELECT * FROM Registration WHERE EventID = %s"
                cursor.execute(query, (eventID,))
                registrations = cursor.fetchall()

                if registrations:
                    tableArray = np.array(registrations)
                    print(pd.DataFrame(tableArray, columns=["RegistrationID", "EventID", "AttendeeID", "EventName", "AttendeeName"]))
                else:
                    print(f"No registrations found for event ID '{eventID}'")
            if option == 4:
                attendeeID = input("Enter the Attendee ID: ")
                query = "SELECT * FROM Registration WHERE AttendeeID = %s"
                cursor.execute(query, (attendeeID,))
                registrations = cursor.fetchall()

                if registrations:
                    tableArray = np.array(registrations)
                    print(pd.DataFrame(tableArray, columns=["RegistrationID", "EventID", "AttendeeID", "EventName", "AttendeeName"]))
                else:
                    print(f"No registrations found for attendee ID '{attendeeID}'")
        except Error as e:
            print(f"Error while printing data: {e}")
