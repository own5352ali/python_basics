data = set()

while True:
    input_1 = input("Enter your data and (q) to exit: ")

    if input_1.lower() == "q":
        break
    else:
        data.add(input_1)

print("\n------------Removing Common Elements------------")
print(f"\n {data}")


