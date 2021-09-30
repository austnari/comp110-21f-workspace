"""PJ00."""


__author__ = "730396074"

from random import randint

player: str
points: int
NAMED_CONSTANT = '\U00002694\U0001F6E1\U0001F3F9'


def greet() -> None:
    """Instructions and getting the player's name."""
    print("Welcome to this adventure game where you decide what to do next.")
    print("Please type 'yes' and 'no' or 'left' and 'right' when necessary.")
    global player
    player = str(input("First off, what is your name, adventurer? "))


def doors() -> int:
    """Choose either door or quit."""
    print(f"{player}, two doors are in front of you, do you choose the left or the right? ")
    x = input("You can type quit if you would like to quit. ")
    if x == "left":
        option1: int = 1
        return option1
    if x == "right":
        option2: int = 2
        return option2
    else:
        option3: int = 0
        return option3
    

def hallway() -> int:
    """Hallway scene."""
    print("You wonder down a dark corridor and find a chest!")
    open = input("Do you open it? ")
    if open == "yes":
        x = 1
        return x
    else:
        x = 2
        return x


def pitfall() -> int:
    """Wrong lever Kronk!"""
    print("As soon as you step through the right door a trapdoor opens below your feet and you fall.")
    print("Surprsingly you've only broken a leg.")
    open = input("You stumble until you come up to a chest, do you open it? ")
    if open == "yes":
        x = 1 
        return x
    else:
        x = 2
        return x


def mystery_box(x: int) -> int:
    """Using randint to give player a random item."""
    weapon = randint(1, 3)
    if weapon == 1:
        print("YOU RECEIVED A SWORD!")
        return weapon
    if weapon == 2:
        print("YOU RECEIVED A SHIELD!")
        return weapon
    if weapon == 3:
        print("YOU RECEIVED A BOW!")
        return weapon


def boss_fight() -> int:
    """Does the player enter the fight."""
    print("With your new weapon in hand you continue on.")
    print("Suddenly, a monster appears!")
    attack = input("Do you fight? ")
    if attack == "yes":
        x = 1 
        return x
    else:
        x = 2
        return x


def fight_time() -> int:
    """Actual fight."""
    print("You attack with your weapon.")
    attack = input("Do you aim for the eyes? ")
    if attack == "yes":
        x = 1 
        return x
    else:
        x = 2
        return x


def gameover() -> None:
    """Gameover loser."""
    print("You have made a decision that has lead to your death...")


def finish() -> None:
    """Non-gameover ending."""
    global player
    player = player
    print(f"Congratulations, {player}! You have completed your adventure whether you liked your ending or not.")
    x = input("Play Again?  yes or no ")
    if x == "yes":
        main()
    if x == "no":
        print("Thanks for playing, have a good day! ")


def main() -> None:
    """Start of the adventure."""
    points = 0
    greet()
    first_decision = doors()
    weapon = 0

    if first_decision == 0:
        points = points - 50
        gameover()

    if first_decision == 1:
        second_decision = hallway()

        if second_decision == 1:
            weapon = mystery_box()
            if weapon == 1:
                print(NAMED_CONSTANT[0])
                points = points + 100
            if weapon == 2:
                print(NAMED_CONSTANT[1])
                points = points + 100
            if weapon == 3:
                print(NAMED_CONSTANT[2])
                points = points + 100
            points = points + 100
        else:
            points = points - 50
        points = points + 100

    if first_decision == 2:
        second_decision = pitfall()

        if second_decision == 1:
            weapon = mystery_box()
            if weapon == 1:
                print(NAMED_CONSTANT[0])
                points = points + 100
            if weapon == 2:
                print(NAMED_CONSTANT[1])
                points = points + 100
            if weapon == 3:
                print(NAMED_CONSTANT[2])
                points = points + 100
            points = points + 100
        else:
            points = points - 50
        points = points - 50

    if weapon > 0: 
        third_decision = boss_fight()
        if third_decision == 1:
            points = points + 100
            fourth_decision = fight_time()
            if fourth_decision == 1:
                print("You blind the monster to give you enough time and get away.")
                points = points + 200
            else:
                print("You decide to not go for its eyes, but during this hesitation the monster attacks and you die...")
                gameover()
    if weapon == 0:
        print("Without anything to fend for yourself you get eaten by rats.")
        points = points - 100
        gameover()
    
    print(f"Total points earned: {points}")
    finish()


if __name__ == "__main__":
    main()