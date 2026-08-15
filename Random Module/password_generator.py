import random
import string

length = int(input("Enter the Length of your Password: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)