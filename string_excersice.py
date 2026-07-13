
# Validate Use Input Excersice
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter the User-Name: ")



if len(username) > 12:
    print("The User-Name should not be more than 12 characters ")

elif not username.find(" ") == -1:
    print("The User-Name must not contain spaces")

elif not username.isalpha():
    print("The User-Name must not contain digits")

else:
    print(f"Welcome! {username}")