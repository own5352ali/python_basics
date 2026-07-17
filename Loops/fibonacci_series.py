
num = int(input("Enter the number for Fibonacci Series: "))

first_num = 0
second_num = 1
next = 0
for i in range (1, num+1):
    next = first_num + second_num
    first_num = second_num
    second_num = next
    print(next)

