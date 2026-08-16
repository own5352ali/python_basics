

calculator = True

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2
    
while calculator:

    print("-------------- Calculator --------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    user = input("What operation you want to perform: ")

    if user == "1":
        num1 = int(input("Enter your First Number: "))
        num2 = int(input("Enter your Second Number: "))
        print(add(num1, num2))

    elif user == "2":
        num1 = int(input("Enter your First Number: "))
        num2 = int(input("Enter your Second Number: "))
        print(subtract(num1, num2))

    elif user == "3":
        num1 = int(input("Enter your First Number: "))
        num2 = int(input("Enter your Second Number: "))
        print(multiply(num1, num2))

    elif user == "4":
        num1 = int(input("Enter your First Number: "))
        num2 = int(input("Enter your Second Number: "))
        print(divide(num1, num2))

    elif user == "5":
        print("---------------- EXIT ----------------")
        calculator = False

    else:
        print("Invalid Option!")