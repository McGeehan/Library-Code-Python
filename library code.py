#importing the library
#FIND 3 BUGS
import random

def guessing_game()

    secret_number = random.randint(1, 100) #assigns a number 1 through 100 to the def secret number 
    
    while True
        guess = int(input("Guess the number between 1 and 100: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else
            print("Congratulations! You guessed it right!")
            break
        
guessing_game()
