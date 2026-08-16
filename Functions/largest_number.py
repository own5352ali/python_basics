
def largest_num():

    largest = None

    for num in range(0, 5):

        num = input("Enter your Number or (q) to exit: ")

        if num.lower() == "q":
            break

        num = int(num)

        if largest is None or num > largest:
            largest = num

    return largest

print("Largest Number: ", largest_num())

