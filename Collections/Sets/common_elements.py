
fruits_1 = set ()
fruits_2 = set ()


while True:

    input_1 = input("Enter your fruits for set 1: and (q) to exit ")

    if input_1.lower() == "q":
        break
    else:
        fruits_1.add(input_1)
print()

print("--------SET 1--------")
for input_1 in fruits_1:
    print(f"{input_1} ", end="")
print("\n")

while True:

    input_2 = input("Enter your fruits for set 2: and (q) to exit ")

    if input_2.lower() == "q":
        break
    else:
        fruits_2.add(input_2)
print()

print("--------SET 2--------")
for input_2 in fruits_2:
    print(f"{input_2} ", end="")

common = fruits_1.intersection(fruits_2)

print("\n")

print("-----------Common Elements-----------")
print(common)
