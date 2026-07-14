
Height = float(input("Enter your Height 'M': "))
Weight = float(input("Enter your Weight in 'Kg': "))

BMI = Weight / pow(Height, 2) 
print(f"Your BMI is: {round(BMI,2)}")

if BMI < 18.5:
    print("Underweight")

elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal Weight")

elif BMI >= 25 and BMI <= 29.9:
    print("Overweight")

else:
    print("Obese")


