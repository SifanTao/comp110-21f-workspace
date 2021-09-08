"""An example of conditional (if-else) statements."""

SECRET: int = 3
#When naming a variable with all uppercase letter, we are intending to be constant and not planning on changing it later on.

print("I'm thinking a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day!!!")
else: 
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You gussed too high!")
    else: 
        print("You gussed too low!")

print("Game over.")