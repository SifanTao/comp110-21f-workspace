"""This program is to ask for two numerical variables and practice relational operators."""

__author__ = "730529631"

number3: int = int(input("Left-hand side: "))
number4: int = int(input("Right-hand side: "))
print(str(number3) + " < " + str(number4) + " is " + str(number3 < number4))
print(str(number3) + " >= " + str(number4) + " is " + str(number3 >= number4))
print(str(number3) + " == " + str(number4) + " is " + str(number3 == number4))
print(str(number3) + " != " + str(number4) + " is " + str(number3 != number4))