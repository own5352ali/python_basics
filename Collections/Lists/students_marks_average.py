
result = []

amnt_of_student = int(input("How many students: "))


for student in range (amnt_of_student):
        name_of_student = input("Enter your name: ")
        chemistry = float(input("Enter your marks for Chemistry: "))
        physics = float(input("Enter your marks for Physics: "))
        mathematics = float(input("Enter your marks for Mathematics: "))
        english = float(input("Enter your marks for English: "))
        computer_science = float(input("Enter your marks for Computer Science: "))

        total = chemistry + physics + mathematics + english + computer_science
        average = (total / 500) * 100

        if   88 <= average <= 100:
                grade = "A"
        elif  74 <= average <= 87:
                grade = "B"
        elif  60 <= average <= 73:
                grade = "C"
        else:
                grade = "F"

        result.append([name_of_student, total, average, grade])


print("-----------Result-----------")
for student in result:
        print(f"Name: {student[0]}" )
        print(f"Total Marks: {student[1]}") 
        print(f"Average: {round(student[2], 2)}%")
        print(f"Grade: {student[3]}")     
        

         