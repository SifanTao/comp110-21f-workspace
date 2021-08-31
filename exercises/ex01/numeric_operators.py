"""This program is to ask for two numerical variables and demonstrate numerical operations."""

__author__ = "730529631"

number1: str = input("Left-hand side: ")
number2: str = input("Right-hand side: ")
print(number1 + " ** " + number2 + " is " + str(int(number1) ** int(number2)))
print(number1 + " / " + number2 + " is " + str(int(number1) / int(number2)))
print(number1 + " // " + number2 + " is " + str(int(number1) // int(number2)))
print(number1 + " % " + number2 + " is " + str(int(number1) % int(number2)))