import random

balance = random.randint(100, 5000)
menu = True

while menu:

    print("------------- MENU System -------------")
    print("1. View Profile")
    print("2. View Balance")
    print("3. Settings")
    print("4. Exit")

    choice = input("Choose an option: ")

    match choice:

        case "1":
            print("--------- PROFILE ---------")
            print("Name: Own Ali")
            print("Age: 20")
            print("Role: Student")

        case "2":
            print("--------- BALANCE ---------")
            print("Your Balance is:", balance)

        case "3":
            print("--------- SETTINGS ---------")
            print("Settings opened.")
            print("1. Change Password")
            print("2. Change Username")

        case "4":
            print("Exiting program...")
            menu = False

        case _:
            print("\nInvalid Input!")
            