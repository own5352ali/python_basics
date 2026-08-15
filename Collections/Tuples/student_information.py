
student = []

no_of_students = int(input("Enter how many students: "))

for university in range (no_of_students):
    name = input("Enter your name: ")
    age = int(input("Age: "))
    student_id = int(input("Enter your Student ID: "))
    department = input("Enter your Department name: ")
    print()
    students = (
       name,
       age,
       student_id,
       department
    )
    student.append(students)

print("-----------Student Information-----------")
for university in student:
        print(f"Name: {university[0]}" )
        print(f"Age: {university[1]}") 
        print(f"Student ID: {university[2]}")
        print(f"Department: {university[3]}")   
        print()
  
