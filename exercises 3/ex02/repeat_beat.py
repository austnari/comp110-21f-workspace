"""Repeating a beat in a loop."""

__author__ = "730396074"


word = input("What beat do you want to repeat? ")
times_repeated = int(input("How many times do you want to repeat it? "))
s = str(word)

if times_repeated > 0:
    while int(times_repeated) > 1:
        times_repeated = times_repeated - 1
        s = s + " " + word
    print(s)
else:
    print("No beat...")