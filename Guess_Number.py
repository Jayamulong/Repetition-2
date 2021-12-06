#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.

import random
#Generate a random number and the user's guess
Number = random.randint(0, 100)
Guess = None

#Use the condition while to repeatedly ask the perfect answer
while Guess != Number:
    Guess = int(input("Guess the number: "))
#Use the if-else statement to execute the conditions
    if Guess > Number:
        print("Greater than")
        continue
    if Guess < Number:
        print("Less Than")
        continue
#If the guess is the same as the number, display the output
    elif Guess == Number:
        print(f"Congrats, the numbers is {Number}")