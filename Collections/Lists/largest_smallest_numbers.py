
num = []

size = int(input("Enter how many Numbers do you want: "))

for i in range(size):
    numbers = int(input(f"Enter the Number {i+1}: "))
    num.append(numbers)

    smallest = num[0]
    largest = num[0]

    for numbers in num:
        if numbers > largest:
            largest = numbers

        if numbers < smallest:
            smallest = numbers


    print(f"Numbers are: {num}")
    print(f"Largest Number: {largest}")
    print(f"Smallest Number: {smallest}")