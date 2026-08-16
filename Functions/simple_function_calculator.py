
def add():

    num1 = int(input("Enter your First Number: "))
    num2 = int(input("Enter your Second Number: "))

    result = num1 + num2 

    return result

def subtract():
    num1 = int(input("Enter your First Number: "))
    num2 = int(input("Enter your Second Number: "))
    
    result = num1 - num2 
    
    return result

def divide():
    num1 = int(input("Enter your First Number: "))
    num2 = int(input("Enter your Second Number: "))
    
    result = num1 / num2 
    
    return result

def multiply():
    num1 = int(input("Enter your First Number: "))
    num2 = int(input("Enter your Second Number: "))
    
    result = num1 * num2 
    
    return result


print(f"Addition is: {add()}")
print(f"Subtraction is: {subtract()}")
print(f"Division is: {divide():.2f}")
print(f"Multiplication is: {multiply()}")


