"""Repeating a beat in a loop."""

__author__ = "730529631"


beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
i: int = 1
x: str = beat + " "
if times > 0: 
    while i < times:
        beat = x + beat
        i = i + 1
    print(beat)
else:
    print("No beat...")