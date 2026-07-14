
units = float(input("Enter the Number of Units Consumed: "))


if units <= 100:
    Bill = units * 10
    print(f"Your Electricity Bill is {round(Bill, 2)}")

elif units > 100 and units <= 200:
    Bill = units * 15
    print(f"Your Electricity Bill is {round(Bill, 2)}")

else:
    Bill = units * 20
    print(f"Your Electricity Bill is {round(Bill, 2)}")
