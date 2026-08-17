
numbers = [4, 7, 14, -5, -17, 1, 18]

pos_num = [num for num in numbers if num >= 0]
neg_num = [num for num in numbers if num < 0]


print("Positive Numbers: ",pos_num)
print("Negative Numbers: ",neg_num)