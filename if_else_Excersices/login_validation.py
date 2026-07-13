
user_name = input("Enter your Username ")
password = input("Enter your Password ")


if user_name == 'admin' and password == '12345':
     print("Login Sucessfull!")

elif user_name != 'admin':
     print("Invalid Username")

elif password != '12345':
     print("Invalid Password")

else:
     print("Invalid Credentials!")