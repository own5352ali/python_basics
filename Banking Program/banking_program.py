
def show_balance(balance):
    print("\n******************************************")
    print(f"Your Balance is: {balance}pkr")
    print("******************************************")

def deposit():
    print("\n******************************************")
    amount = int(input("Enter your Amount you want to Deposit: "))
    print("******************************************")

    if amount < 0:
        print("\n******************************************")
        print("That's not a Valid Amount")
        print("******************************************")

    else:
        return amount

def withdraw(balance):
    print("\n******************************************")
    amount = int(input("Enter your Amount you want to Withdraw: "))
    print("******************************************")

    if amount > balance:
        print("\n******************************************")
        print("Insufficient Funds...")
        print("******************************************")

    elif amount < 0:
        print("\n******************************************")
        print("The Amount must be greater than 0...")
        print("******************************************")

    else:
        return amount



def main():
    balance = 0
    bank = True

    while bank:
            print("\n******************************************")
            print("------------- Banking System -------------")
            print("******************************************")

            print("\n******************************************")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("******************************************")
        
            choice = input("Enter your choice: ")
        
            match choice:
    
                case "1":
                   show_balance(balance)
    
                case "2":
                    balance += deposit()
    
                case "3":
                    balance -= withdraw(balance)
    
                case "4":
                    print("------------- Exiting -------------")
                    print("\n******************************************")
                    print("Thank You! Have A Nice Day!")
                    print("******************************************")
                    bank = False
    
                case _:
                    print("Invalid Input!")
          
if __name__ == '__main__':
    main()                 
    