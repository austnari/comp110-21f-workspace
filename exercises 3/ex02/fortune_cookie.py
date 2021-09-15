"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730396074"

from random import randint

fortune_one = ("A mysterious person will come into your life.")
fortune_two = ("Your favorite franchise will get a new movie.")
fortune_three = ("You will soon go on an adventure.")
fortune_four = ("You will stub your toe today.")

i = int(randint(1, 4))

print("Your fortune cookie says...")

if i == 1:
    print(fortune_one)
else:
    if i == 2:
        print(fortune_two)
    else:
        if i == 3:
            print(fortune_three) 
        else:
            print(fortune_four)

print("Now, go spread postive vibes!")