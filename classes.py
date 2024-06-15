import mysql.connector
from mysql.connector import Error
import numpy as np
import pandas as pd

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="prnv2005",
        database="eventDBMS"
    )

    cursor = conn.cursor()

except Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)

class Event:

    def __init__(self, eventName, date, location):
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

class Attendees:

    def __init__(self, attendeeName, email):
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
        except Error as e:
            print(f"Error creating Attendees table: {e}")

    def AddValues(self):
        try:
            insertData = """
            INSERT INTO Attendees (AttendeeName, AttendeeEmail) VALUES (%s, %s)  
            """
            data = (self.attendeeName, self.email)
            cursor.execute(insertData, data)
            conn.commit()
        except Error as e:
            print(f"Error adding Attendees values: {e}")

    def ModifyValues(self, option):
        try:
            if option == 1:
                nattendeeName = input("Enter the new Attendee Name : ")
                modifyData = "UPDATE Attendees SET AttendeeName = %s WHERE AttendeeName = %s"
                cursor.execute(modifyData, (nattendeeName, self.attendeeName))
                self.attendeeName = nattendeeName
                conn.commit()
            elif option == 2:
                nattendeeEmail = input("Enter the new Attendee Email : ")
                modifyData = "UPDATE Attendees SET AttendeeEmail = %s WHERE AttendeeEmail = %s"
                cursor.execute(modifyData, (nattendeeEmail, self.email))
                self.email = nattendeeEmail
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error modifying Attendees: {e}")

    def DeleteValues(self, option):
        try:
            if option == 1:
                dattendeeName = input("Enter the Attendee Name : ")
                deleteData = "DELETE FROM Attendees WHERE AttendeeName = %s"
                cursor.execute(deleteData, (dattendeeName,))
                conn.commit()
            elif option == 2:
                demail = input("Enter the Attendee Email : ")
                deleteData = "DELETE FROM Attendees WHERE AttendeeEmail = %s"
                cursor.execute(deleteData, (demail,))
                conn.commit()
            else:
                print("Invalid Option")
        except Error as e:
            print(f"Error deleting Attendees: {e}")

    def PrintData(self, option):
        try:
            if option == 1:
                cursor.execute("SELECT * FROM Attendees")
                rows = cursor.fetchall()

                tableArray = np.array(rows)
                print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))
            if option == 2:
                attendeeName = input("Enter the Attendee Name: ")
                query = "SELECT * FROM Attendees WHERE AttendeeName = %s"
                cursor.execute(query, (attendeeName,))
                attendee = cursor.fetchone()

                if attendee:
                    tableArray = np.array([attendee])
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))
                else:
                    print(f"No attendee found with name '{attendeeName}'")
            if option == 3:
                attendeeEmail = input("Enter the Attendee Email: ")
                query = "SELECT * FROM Attendees WHERE AttendeeEmail = %s"
                cursor.execute(query, (attendeeEmail,))
                attendees = cursor.fetchall()

                if attendees:
                    tableArray = np.array(attendees)
                    print(pd.DataFrame(tableArray, columns=["AttendeeID", "AttendeeName", "AttendeeEmail"]))
                else:
                    print(f"No attendees found with email '{attendeeEmail}'")
        except Error as e:
            print(f"Error while printing data: {e}")

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

    def CreateTriggers(self):
        try:
            create_event_trigger = """
            CREATE TRIGGER before_event_delete
            BEFORE DELETE ON Event
            FOR EACH ROW
            BEGIN
                DELETE FROM Registration WHERE EventID = OLD.EventID;
            END
            """
            cursor.execute(create_event_trigger)
            conn.commit()

            create_attendee_trigger = """
            CREATE TRIGGER before_attendee_delete
            BEFORE DELETE ON Attendees
            FOR EACH ROW
            BEGIN
                DELETE FROM Registration WHERE AttendeeID = OLD.AttendeeID;
            END
            """
            cursor.execute(create_attendee_trigger)
            conn.commit()

            create_event_update_trigger = """
            CREATE TRIGGER before_event_update
            BEFORE UPDATE ON Event
            FOR EACH ROW
            BEGIN
                UPDATE Registration SET EventName = NEW.EventName WHERE EventID = OLD.EventID;
            END
            """
            cursor.execute(create_event_update_trigger)
            conn.commit()

            create_attendee_update_trigger = """
            CREATE TRIGGER before_attendee_update
            BEFORE UPDATE ON Attendees
            FOR EACH ROW
            BEGIN
                UPDATE Registration SET AttendeeName = NEW.AttendeeName WHERE AttendeeID = OLD.AttendeeID;
            END
            """
            cursor.execute(create_attendee_update_trigger)
            conn.commit()

        except Error as e:
            print(f"Error creating triggers: {e}")

# Example usage:
event = Event("Conference 2024", "2024-10-15", "New York")
event.CreateTable()
event.AddValues()

attendee = Attendees("John Doe", "john@example.com")
attendee.CreateTable()
attendee.AddValues()

registration = Registration()
registration.CreateTable()
registration.AddValues(1, 1, "Conference 2024", "John Doe")
registration.CreateTriggers()
