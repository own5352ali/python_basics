import random


game = True

while game:
    
    number = random.randint(1,10)

    guess = int(input("Enter your guess: "))

    if guess < number:
        print(f"The Number is too high! Attempt Again: {number} ")

    elif guess > number:
        print(f"The Number is too Low! Attempt Again: {number} ")

    else:
        print(f"You guessed the Right Answer!{number}")
        print("--------- EXITING ---------")
        game = False