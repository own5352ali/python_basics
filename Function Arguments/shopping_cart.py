def shopping_cart(*args):

    print("---------- Shopping Cart ----------")

    for product in args:
        print(f"Product: {product}")

    print(f"Total Products: {len(args)}")


products = []

while True:
    product = input("Enter your Product name (q to exit): ")

    if product.lower() == "q":
        break

    products.append(product)


shopping_cart(*products)