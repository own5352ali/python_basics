
price = int(input("Enter the price for your selected item: "))
discounted_percentage = int(input("Enter the discount percentage "))

#discount_amount = price * (discounted_percentage / 100)
#discounted_price = price - discount_amount 

if discounted_percentage == 0:
    print("Invalid discount")

else:
    discount_amount = price * (discounted_percentage / 100)
    discounted_price = price - discount_amount 
    print(f"Final Discounted Price is: {discounted_price} Rs")
       