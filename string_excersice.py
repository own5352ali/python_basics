
# Validate Use Input Excersice
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain spaces

username = input("Enter the User-Name: ")



if len(username) > 12:
    print("The User-Name should not be more than 12 characters ")

else:
    print(f"Welcome! {username}")