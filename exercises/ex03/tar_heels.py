"""An exercise in remainders and boolean logic."""

__author__ = "730396074"

i = int(input("Enter an int: "))
two = int(i % 2)
seven = int(i % 7)

if two + seven == 0:
    print("TAR HEELS")
else:
    if i % 2 == 0:
        print("TAR")
    if i % 7 == 0:
        print("HEELS")
    else:
        print("CAROlINA")