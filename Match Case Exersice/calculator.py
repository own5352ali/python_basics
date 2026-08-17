
calculations = True
def calculator():
    while calculations:

        print("---------------- CALCULATOR ----------------")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Choose an operation: ")

        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))

        match choice:
                case "1": 
                    result = num1 + num2
                    print("Your Addition is: ", result)
                
                case "2": 
                    result = num1 - num2
                    print("Your Subtraction is: ", result)
                
                case "3":
                    result = num1 * num2
                    print("Your Multiplication is: ", result)
                
                case "4": 
                    result = num1 / num2
                    print("Your Division is: ", result)
                
                case _:
                    print("Invalid Input")
                    print("-------------- EXITING --------------")
                    break
calculator()
        
        
        
        
        

