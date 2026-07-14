
age = int(input("Enter your Age: "))

print(f"Your Age is {age}")

if age < 13:
    print("You are a Child")

elif age >= 13 and age <= 17:
    print("You are Teenager")

elif age >= 18 and age <= 59:
    print("You are Adult")

else:
    print("You are a Senior Citizen")