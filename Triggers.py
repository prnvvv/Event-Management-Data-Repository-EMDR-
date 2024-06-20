from mysqlConnector import Cursor
from mysql.connector import Error
import numpy as np
import pandas as pd

conn, cursor = Cursor()

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

