
product = {
    "Laptop":{
        "id" : "101",
        "price" : 200000,
        "quantity" : "15",
        "category" : "Electronics"
    }, 

    "Smart Phones":{
        "id" : "102",
        "price" : 45000,
        "quantity" : "29",
        "category" : "Electronics"
    }, 

    "Fridge":{
        "id" : "103",
        "price" : 72000,
        "quantity" : "5",
        "category" : "Electrical"
    }
}

product_inventory = True

while product_inventory:

    print("-------------- PRODUCT INVENTORY --------------")

    print("1. Add Product")
    print("2. Search Product")
    print("3. View Products")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. EXIT")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your Product's name: ")
        id = int(input("Enter I'D for your Product: "))
        price = float(input("Enter the price for your Product: "))
        quantity = int(input("Enter the quantity available in your Stock: "))
        category = input("Enter the Category in which your Product lies: ")

        details = {
            "id" : id,
            "price" : price,
            "quantity" : quantity,
            "category" : category
        }

        product[name] = details
        print("YOUR PROUCT HAS BEEN ADDED TO YOUR INVENTORY!")

    elif choice == "2":
        name = input("Enter the Product you want to Search: ")
        print(product.get(name))

    elif choice == "3":
        for name, details in product.items():
            print(name, ":", details)

    elif choice == "4":
        name = input("Enter the Product you want to Update: ")
        new_id = int(input("Enter I'D for your Product: "))
        new_price = float(input("Enter the price for your Product: "))
        new_quantity = int(input("Enter the quantity available in your Stock: "))
        new_category = input("Enter the Category in which your Product lies: ")

        details = {
                    "id" : new_id,
                    "price" : new_price,
                    "quantity" : new_quantity,
                    "category" : new_category
                }
        product.update({name : details} )
        print("YOUR PRODUCT DATA HAS BEEN UPDATED IN YOUR INVENTORY!")

    elif choice == "5":
        name = input("Enter the Product you want to Delete from your Inventory: ")
        print(product.pop(name))
        print("YOUR PRODUCT HAS BEEN SUCCESSFULLY DELETED FROM THE INVENTORY!")

    elif choice == "6":
        print("---------- EXITING ----------")
        product_inventory = False