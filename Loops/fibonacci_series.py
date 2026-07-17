
num = int(input("Enter the number for Fibonacci Series: "))

first_num = 0
second_num = 1

if num <= 0:
    print("Please enter a positive number.")

elif num == 1:
    print(first_num)

else:
    print(first_num)
    print(second_num)

for i in range (1, num+1):
    next = first_num + second_num
    first_num = second_num
    second_num = next
    print(next)

