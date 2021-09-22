"""Finding duplicate letters in a word."""

__author__ = "730529631"


word: str = input("Enter a word: ") 
result: bool = False
i: int = 0
x: int = 0
character: str = word
while i < len(word):
    x = i + 1
    character = word[i]
    while x < len(word):
        if character == word[x]:
            result = True
        x = x + 1
    i = i + 1
    
print("Found duplicate: " + str(result))