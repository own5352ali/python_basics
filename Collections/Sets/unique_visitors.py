
visitor = set()

while True:
    input_1 = input("Enter your data and (q) to exit: ")

    if input_1.lower() == "q":
        break
    else:
        visitor.add(input_1)

print("\n------------Unique Visitors------------")
print(f"\n {visitor}")
print("Your total Visiors are: ", len(visitor))
