
contacts = {
    "Aun Ali": "+923323385141",
    "Batul": "+924795804853",
    "Usman": "+928708970949",
    "Raj": "+924784897384"
}

contact_book = True

while contact_book:
    print ("------------ MY CONTACT BOOK ------------")
    print ("1. Add Contact")
    print ("2. Search Contact")
    print ("3. Update Contact")
    print ("4. Delete Contact")
    print ("5. Show Contacts")
    print ("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        contact_num = input("Enter the Contact Number: ")
        contacts[name] = contact_num
        print("Contact Added successfully!")

    elif choice == "2":
       name = input("Enter the Name you want to search: ")
       print (contacts.get(name))

    elif choice == "3":
        name = input("Enter the Name you want to update: ")
        new_contact_num = input("Enter your updated Contact Number: ")
        contacts.update({name:new_contact_num})
        print("Contact Updated successfully!")

    elif choice == "4":
        name = input("Enter the Name you want to delete: ")
        print (contacts.pop(name))
        print("Contact Deleted successfully!")

    elif choice == "5":
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == "6":
        print ("-------Exiting-------")
        contact_book = False

    

