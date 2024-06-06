import mysql.connector


conn = mysql.connector.connect(
    host="localhost",        
    user="root",    
    password="prnv2005",
    database = "eventDBMS"
)

cursor = conn.cursor()

class Event:

    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.data = [(self.name, self.date, self.location)]

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

event1 = Event("Prnv", "2005/09/12", "triplicane")
event1.createTable()
event1.addValues()

 