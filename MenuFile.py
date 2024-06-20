from Triggers import CreateTriggers
from EventsClass import Event
from AttendeesClass import Attendees
from RegistrationClass import Registration

print()

print("Welcome to Event Database Management System")

print()

print("MENU FOR ACCESSING:")

print("1. Events")
print("2. Attendees")
print("3. Registrations")

print()

options = int(input("Enter your desired option: "))

print()

if options == 1:
    EventObject = Event()
    print("EVENTS")
    print()
    print("MENU")
    print("1. To create a Events Table (if doesnt exist)")
    print("2. To add an Event")
    print("3. To modify an Event")
    print("4. To delete an event")
    print("5. To print the details of the Event/Events")
    print()