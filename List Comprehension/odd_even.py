
numbers = [4, 7, 14, -5, -17, 1, 18]

even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 == 1]

print("Even Numbers: ",even_num)
print("Odd Numbers: ", odd_num)