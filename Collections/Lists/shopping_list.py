
shopping_list = []


while True:
    item = input(("Enter the item you want to buy or Enter (q) to exit: "))
    if item.lower() == "q":
        break
    else:
        shopping_list.append(item)

print("---- Shopping List ----")

for item in shopping_list:
    print(item)