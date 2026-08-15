
items = ["Fruits", "Vegetables", "cereals", "popcorn", "Drinks", "Furniture", "Sofa"]

item_list = 0
found = False
preference = input(("Enter your item to search: "))

while item_list < len(items):

    if items[item_list].lower() == preference.lower():
        found = True
        break

    item_list += 1

if found:
        print("The item is found!")
        print(f"The item was found at index {item_list}: ")
else:
        print("The item is not in your list!")


