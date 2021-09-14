"""Finding duplicate letters in a word."""

__author__ = "730529631"


word: str = input("Enter a word: ")
i: int = 0
x: int = 0

while i < len(word):
    x = i + 1
    while x < len(word):
        if word[i] == word[x]:
            print("Found duplicate: True")
            quit()
        else:
            x = x + 1
    i = i + 1
    

print("Found duplicate: False")




