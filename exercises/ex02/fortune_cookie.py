"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730529631"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
m1: str = str("Have a nice day. ")
m2: str = str("Tommorow will be better. ")
m3: str = str("There's light at the end of the road. ")
m4: str = str("You are perfect just the way you are. ")
result: int = randint(1, 4)
if result == 1:
    print(m1)
else:
    if result == 2:
        print(m2)
    else: 
        if result == 3:
            print(m3)
        else: 
            print(m4)


print("Now, go spread positive vibes!")