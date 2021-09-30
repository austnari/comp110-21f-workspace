"""An exercise in remainders and boolean logic."""

__author__ = "730396074"

i = int(input("Enter an int: "))
two = int(i % 2)
seven = int(i % 7)
s = 0

if two + seven == 0:
    print("TAR HEELS")
    s = s + 1
else:
    if i % 2 == 0:
        print("TAR")
        s = s + 1
    if i % 7 == 0:
        print("HEELS")
        s = s + 1
if s == 0:
    print("CAROLINA")