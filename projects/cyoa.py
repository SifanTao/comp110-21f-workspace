"""A Roll-playing Game Project."""

__author__ = "730529631"
# Does the end experience option have to be for the function call or procedural call? 
# Can the procedural function return a int value as well? Does it have to return to a None type?
# Do the points have to accumulate evertime going into a new direction? Can it start from the beginning eachtime a new direction is called?


points: int = 0
player: str = ""
NAMED_CONSTANT1: str = "\U0001F631"
NAMED_CONSTANT2: str = "\U0001F608"


def main() -> None:
    """Main Function."""
    global points
    greet()
    points2: int = 1
    while points2 > 0:
        role: str = str(input(f"{player}, your current score is {points}. Please choose a role to continue: warrior, dragon, or None? "))
        if role == "warrior":
            path1()
        elif role == "dragon":
            points = path2(points)
        else:
            points2 = points2 - 1
        print(f"Your score is {points}. See you next time, {player}!")


def greet() -> None:
    """Greet Function."""
    global player
    player = str(input("Nice to meet you! You have entered a new world! Loyalty or Power? That is the question! What is your name? "))
    hello: str = str(f"Nice to meet you, {player}!")
    print(hello)


def path1() -> None:
    """Direction 1: procedural call."""
    global points
    points = points + 1
    print(f"Great choice {player}! Now, your duty is to protect the country from the dragons.")
    weapon: str = str(input(f"Warrior {player}, please pick a weapon: sword or shield? "))
    if weapon == "sword":
        points = points + 1
        print("The dragons are invading the castle!")
        defence: str = str(input("Would you like to use your sword: yes or no? "))
        if defence == "yes":
            points = points + 1
            while points > 0:
                points = points - 1
                print("More coming!")
            print(f"Congrats, warrior {player}! You have defeated the dragons! However, great success came with a price. You have lost all your points. ")
        else:
            print(f"The dragons took over the castle {NAMED_CONSTANT1}")
    elif weapon == "shield":
        points = points + 1
        print(f"You have successfully avoid the fire ball. Now, warrior {player} go ask for reinforcement!")


def path2(points: int) -> int:
    """Direction 2: function call."""
    points = points + 1
    print(f"You are {player}, the Great Dragon. Time for some Human-games! {NAMED_CONSTANT2}")
    fire: int = 0
    game: str = str(input("Gather energy for your fire balls? yes or no "))
    if game == "yes":
        points = points + 1
        from random import randint
        fire = randint(1, 3)
        while fire > 0:
            print("Let them burn!!")
            points = points + 1
            fire = fire - 1
        print("The city is yours now!")
        return points 
    else: 
        print("Maybe next time!")
        return points


if __name__ == "__main__":
    main()