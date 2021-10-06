import random

choice = "Y"

while choice == "Y" or choice == "y":
    
    number = random.randint(1,100)
    guess = None
    numberOfGuess = 0
    
    while guess != number:
        try:
            guess = int(input("Guess the number between 1 to 100 : "))
        except:
            print("Invalid input!\n")
            break

        numberOfGuess += 1
            
        if guess > 100 or guess < 1:
            print("Please guess between 1 to 100 only...\n")

        elif guess == number:
            print("\n*****Congrats You did it!*****\n")
            print("Number of Guesses = ", numberOfGuess)
            break

        elif guess > number:
            print("Guessed too high!!!\n")

        elif guess < number:
            print("Guessed too low!!!\n")
    
    while True:
        choice = input("Want play again? Press Y for Yes and N for No....")
        if choice == "Y" or choice == "y" or choice == "N" or choice == "n":
            break