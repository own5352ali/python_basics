
employee = {
    "Aun Ali" :{
      "id" : "67539" ,
      "age" : 20,
      "department" : "IT", 
      "salary" : 1200000
    },
    "Batul" :{ 
        "id" : "67521", 
       "age" : 20, 
       "department" : "Accountant", 
       "salary" : 100000
    },
    "Ammar" :{
       "id" : "67853", 
       "age" : 21, 
       "department" : "Technician",  
       "salary" : 50000
    },
    "Shabbir" :{ 
       "id" : "67543",
       "age" : 22,  
       "department" : "Supervisor", 
       "salary" : 250000
    }
}

employee_database = True

while employee_database:
    print("--------- EMPLOYEE DATABASE ---------")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the Name: ")
        id = int(input("Enter the I'D: "))
        age = int(input("Enter the Age: "))
        department = input("Enter the Department Name: ")
        salary = float(input("Enter the Salary: "))
        details = {
        "id": id,
        "age": age,
        "department": department,
        "salary": salary
    }
        employee[name] = details
        print("EMPLOYEE ADDED SUCCESSFULLY!")

    elif choice == "2":
        for name, details in employee.items():
            print(name, ":", details )
    
    elif choice == "3":
        name = input("Enter the Name you want to Search: ")
        print (employee.get(name))

    elif choice == "4":
        name = input ("Enter the Name you want to Update ")
        new_id = int(input("Enter the I'D: "))
        new_age = int(input("Enter the Age: "))
        new_department = input("Enter the Department Name: ")
        new_salary = float(input("Enter the Salary: "))
        details = {
                "id": new_id,
                "age": new_age,
                "department": new_department,
                "salary": new_salary
            }
        employee.update({name : details})
        print ("EMPLOYEE UPDATED SUCCESSFULLY!")

    elif choice == "5":
        name = input("Enter the Name you want to delete: ")
        print (employee.pop(name))
        print("EMPLOYEE DELETED SUCCESSFULLY!")
    
    elif choice == "6":
        print ("-------Exiting-------")
        employee_database = False    