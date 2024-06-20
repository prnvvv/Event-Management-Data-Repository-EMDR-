from Triggers import CreateTriggers
from EventsClass import Event 
from AttendeesClass import Attendees
from RegistrationClass import Registration

print()

print("Welcome to Event Database Management System")

print()

while True:
        
    print("MENU FOR ACCESSING:")

    print("1. Events")
    print("2. Attendees")
    print("3. Registrations")
    print("4. Exit")

    print()

    options = int(input("Enter your desired option: "))

    print()

    if options == 1:
        print("EVENTS")
        print()
        print("MENU")
        print("1. To create a Events Table (if doesnt exist)")
        print("2. To add an Event")
        print("3. To modify an Event")
        print("4. To delete an event")
        print("5. To print the details of the Event/Events")
        print("6. Exit")

        print()

        eventOption = int(input("Enter your desired option: "))

        print()

        while True:
            if eventOption == 1:
                Event.CreateTable()
            elif eventOption == 2:
                nEvents = int(input("Enter the number of datas you want to add: "))
                for i in range(nEvents):
                    eventName = input("Enter the Event Name: ")
                    eventDate = input("Enter the Event Date (yyyy/mm/dd): ")
                    eventLocation = input("Enter the Event Location: ")
                    Event(eventName, eventDate, eventLocation).AddValues()
            elif eventOption == 3:
                print("MODIFY MENU")
                print()
                print("1. To update Event Name")
                print("2. To update Event Date")
                print("3. To update Event Location")
                print()
                modifyEventOption = int(input("Enter the desired option: "))
                Event().ModifyValues(modifyEventOption)


