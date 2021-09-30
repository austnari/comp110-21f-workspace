"""PJ00."""


__author__ = "730396074"

from random import randint

points: int = 0
player: str = greet()
NAMED_CONSTANT = '\U00002694\U0001F6E1\U0001F3F9'



def greet() -> None:
    """Greeting the gamer."""
    global player
    player: str = input("What is your name? ")
    print("Hello, " + x + ".")
    print("You will now be participating in an adventure where you decide what happens next.")
    print("Please use 'yes' and 'no' or 'left' and 'right' responses when necessary.  Thank you!")


def doors():
    """Two doors or quit."""
    print("Two doors are in front of you.")
    x = input("Do you pick the left one or the right one?  ...or quit like a scaredy cat? (you can type quit to quit if you're scared) ")
    if x == "left":
        option1: int = 1
        return option1
    if x == "right":
        option1: int = 2
        return option1
    else:
        option1: int = 0
        return option1


def hallway():
    """Hallway scene."""
    print("You wonder down a dark corridor and find a chest!")
    open = input("Do you open it? ")
    if open == "yes":
        x = 1
        return x
    else:
        x = 2
        return x


def pitfall():
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


def mystery_box():
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


def monster():
    """Monster boss battle."""
    x = 0
    decision = input("Quick! You must decide do you stay and fight? yes or no")
    if decision == "yes":
        boss_fight()
    if decision == "no":
        death_scene()


def death_scene():
    "Default death scene."
    print("You have chosen the wrong path, and due to your actions you have died.")
    print("Rest in pieces.")
    gameover()


def gameover():
    """Gameover loser."""
    print("You lost...")
    print(f"Total points earned: {adventure_points}")
    x = input("Play Again?  yes or no ")
    if x == "yes":
        main()
    if x == "no":
        print("Thanks for playing, have a good day! ")


def main():
    """Starting the adventure/journey/odyssey/quest/campaign."""
    NAMED_CONSTANT = '\U00002694\U0001F6E1\U0001F3F9'
    weapon = ()

    first_decision = doors()

    if first_decision == 0:
        gameover()

    if first_decision == 1:
        second_decision = hallway()

        if second_decision == 1:
            weapon = mystery_box()
            if weapon == 1:
                print(NAMED_CONSTANT[0])
                weapon = NAMED_CONSTANT[0]
                adventure_points = adventure_points + 100
            if weapon == 2:
                print(NAMED_CONSTANT[1])
                weapon = NAMED_CONSTANT[1]
                adventure_points = adventure_points + 100
            if weapon == 3:
                print(NAMED_CONSTANT[2])
                weapon = NAMED_CONSTANT[2]
                adventure_points = adventure_points + 100
            adventure_points = adventure_points + 100
        else:
            death_scene()
            adventure_points = adventure_points - 50
        adventure_points = adventure_points + 100
        
    if first_decision == 2:
        second_decision = pitfall()

        if second_decision == 1:
            weapon = mystery_box()
            if weapon == 1:
                print(NAMED_CONSTANT[0])
                weapon = NAMED_CONSTANT[0]
                adventure_points = adventure_points + 100
            if weapon == 2:
                print(NAMED_CONSTANT[1])
                weapon = NAMED_CONSTANT[1]
                adventure_points = adventure_points + 100
            if weapon == 3:
                print(NAMED_CONSTANT[2])
                weapon = NAMED_CONSTANT[2]
                adventure_points = adventure_points + 100
            adventure_points = adventure_points + 100
        else:
            print(f"{player}, {player}, {player} you suck")
            death_scene()
            adventure_points = adventure_points - 50
        adventure_points = adventure_points - 50
    print(f"You pick up your new {weapon} and head down the dark hall in front of you.")
    print(f"{player}, you begin to hear a loud noise... you begin to wonder, is it the wind or a beast breathing?")
    print("Suddenly a monster emerges from the darkness!")
    third_decision = monster()
    if third_decison == 1:
        (print("hi"))

if __name__ == "__main__":
    main()
