import math

Chemistry = float(input("Enter the marks for Chemistry: "))
English = float(input("Enter the marks for English: "))
Physics = float(input("Enter the marks for Physics: "))
Mathematics = float(input("Enter the marks for Mathematics: "))

Total = Chemistry+English+Physics+Mathematics
Result = Total/4

print(f"{Result}%")

if Result >= 88 and Result <= 100:
     print("The grade is 'A+' ")

elif Result >= 81 and Result <= 87:
     print("The grade is 'A' ")

elif Result >= 74 and Result <= 80:
     print("The grade is 'B' ")

elif Result >= 60 and Result <= 73:
     print("The grade is 'C' ")

elif Result >= 50 and Result <= 59:
     print("The grade is 'D' ")

elif Result <= 49 and Result >=0:
      print("The grade is 'F' ")

else:
     print("Invalid Credentials")