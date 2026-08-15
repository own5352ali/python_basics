students = {
    "Aun Ali":{
        "roll_number" : "101",
        "age" : 15,
        "students_class" : "10",
        "marks" : "82%"
    }, 

    "Batul":{
        "roll_number" : "102",
        "age" : 14,
        "students_class" : "10",
        "marks" : "94%"
    }, 

    "Sakina":{
        "roll_number" : "103",
        "age" : 14,
        "students_class" : "9",
        "marks" : "81%"
    },

    "Abizer":{
        "roll_number" : "104",
        "age" : 15,
        "students_class" : "9",
        "marks" : "78%"
        }
}

student_record = True

while student_record:

    print("-------------- STUDENT RECORDS --------------")

    print("1. Add Student Records")
    print("2. Search Records")
    print("3. View Student Records")
    print("4. Update Records")
    print("5. Delete Records")
    print("6. EXIT")

    choice = input("Enter your choice: ")

    if choice == "1":
            name = input("Enter your Student's name: ")
            roll_number = int(input("Enter Student's Roll Number: "))
            age = int(input("Enter Student's Age: "))
            students_class = int(input("Enter Student's Class: "))
            marks = input("Enter the Marks scored by the Student: ")
    
            details = {
                "roll_number" : roll_number,
                "age" : age,
                "students_class" : students_class,
                "marks" : marks
            }
    
            students[name] = details
            print("YOUR STUDENT'S RECORD HAS BEEN ADDED TO UOUR INVENTORY!")

    elif choice == "2":
            name = input("Enter the Product you want to Search: ")
            print(students.get(name))

    elif choice == "3":
            for name, details in students.items():
                print(name, ":", details)

    elif choice == "4":
            name = input("Enter your Student's name: ")
            new_roll_number = int(input("Enter Student's Roll Number: "))
            new_age = int(input("Enter Student's Age: "))
            new_students_class = int(input("Enter Student's Class: "))
            new_marks = input("Enter the Marks scored by the Student: ")
    
            details = {
                        "roll_number" : new_roll_number,
                        "age" : new_age,
                        "students_class" : new_students_class,
                        "marks" : new_marks
                    }
            students.update({name : details} )
            print("YOUR STUDENT'S RECORD HAS BEEN UPDATED IN YOUR INVENTORY!")

    elif choice == "5":
            name = input("Enter the Product you want to Delete from your Inventory: ")
            print(students.pop(name))
            print("YOUR STUDENT'S RECORD HAS BEEN SUCCESSFULLY DELETED FROM THE INVENTORY!")
    
    elif choice == "6":
            print("---------- EXITING ----------")
            student_record = False