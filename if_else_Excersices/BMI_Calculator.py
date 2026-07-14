
Height = float(input("Enter your Height 'M': "))
Weight = float(input("Enter your Weight in 'Kg': "))

BMI = Weight / pow(Height, 2) 

if BMI < 18.5:
    print(f"{round(BMI,2)}")
    print("Underweight")

elif BMI >= 18.5 and BMI <= 24.9:
    print(f"{round(BMI,2)}")
    print("Normal Weight")

elif BMI >= 25 and BMI <= 29.9:
    print(f"{round(BMI,2)}")
    print("Overweight")

else:
    print(f"{round(BMI,2)}")
    print("Obese")


