

name = input("Enter student name: ")
age = input("Enter age: ")
course = input("Enter course: ")

def student_info(name, age, course, city="Karachi"):

    print("------------------------")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"City: {city}")

student_info(name = name,
             age = age,
             course = course)