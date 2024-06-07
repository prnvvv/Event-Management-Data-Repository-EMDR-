import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="prnv2005",
    database="eventDBMS"
)

cursor = conn.cursor()

class Event:

    def __init__(self, eventName, date, location):
        self.eventName = eventName
        self.date = date
        self.location = location
        self.data = [(self.eventName, self.date, self.location)]

    def createTable(self):
        eventTable = """
        CREATE TABLE IF NOT EXISTS Event(
        EventID INT AUTO_INCREMENT PRIMARY KEY,
        EventName VARCHAR(255) NOT NULL,
        Date DATE NOT NULL,
        Location VARCHAR(255) NOT NULL)"""
        cursor.execute(eventTable)
        conn.commit()

    def addValues(self):
        insertData = """
        INSERT INTO Event (EventName, Date, Location) VALUES (%s, %s, %s)
        """
        for data in self.data:
            cursor.execute(insertData, data)
        conn.commit()

class Attendees:

    def __init__(self, attendeeName, email):
        self.attendeeName = attendeeName
        self.email = email
        self.data = [(self.attendeeName, self.email)]

    def createTable(self):
        attendeeTable = """
        CREATE TABLE IF NOT EXISTS Attendees(
        AttendeeID INT AUTO_INCREMENT PRIMARY KEY,
        AttendeeName VARCHAR(255) NOT NULL,
        AttendeeEmail VARCHAR(255) NOT NULL)"""
        cursor.execute(attendeeTable)
        conn.commit()

    def addValues(self):
        insertData = """
        INSERT INTO Attendees (AttendeeName, AttendeeEmail) VALUES (%s, %s)  
        """
        for data in self.data:
            cursor.execute(insertData, data)
        conn.commit()

class Registration(Event, Attendees):

    def __init__(self, eventName, date, location, attendeeName, email):
        Event.__init__(self, eventName, date, location)
        Attendees.__init__(self, attendeeName, email)

    def createTable(self):
        registrationTable = """
        CREATE TABLE IF NOT EXISTS Registration(
        RegistrationID INT AUTO_INCREMENT PRIMARY KEY,
        EventID INT,
        AttendeeID INT,
        EventName VARCHAR(255),
        AttendeeName VARCHAR(255),
        FOREIGN KEY (EventID) REFERENCES Event(EventID),
        FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID))"""
        cursor.execute(registrationTable)
        conn.commit()

    def addValues(self):
        Event.addValues(self)
        Attendees.addValues(self)

        cursor.execute("SELECT EventID FROM Event WHERE EventName = %s AND Date = %s AND Location = %s",
                       (self.eventName, self.date, self.location))
        EventID = cursor.fetchone()[0]

        cursor.execute("SELECT AttendeeID FROM Attendees WHERE AttendeeName = %s AND AttendeeEmail = %s",
                       (self.attendeeName, self.email))
        AttendeeID = cursor.fetchone()[0]

        insert_data = """
        INSERT INTO Registration (EventID, AttendeeID, EventName, AttendeeName) VALUES (%i, %i, %s, %s)
        """
        cursor.execute(insert_data, (EventID, AttendeeID, self.eventName, self.attendeeName))
        conn.commit()

event = Event("Conference", "2024-07-01", "New York")
event.createTable()
event.addValues()

attendee = Attendees("John Doe", "john.doe@example.com")
attendee.createTable()
attendee.addValues()

registration = Registration("Conference", "2024-07-01", "New York", "John Doe", "john.doe@example.com")
registration.createTable()
registration.addValues()
