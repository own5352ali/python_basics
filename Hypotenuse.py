import math

a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The Hypotenuse of the Right-Angled Triangle is: {round(c, 1)}")