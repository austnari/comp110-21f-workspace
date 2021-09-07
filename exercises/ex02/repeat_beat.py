"""Repeating a beat in a loop."""

__author__ = "730396074"


word = (input("What beat do you want to repeat? "))
times_repeated = int(input("How many times do you want to repeat it? "))

if times_repeated > 0:
    while times_repeated > 0:
        print(word)
        times_repeated = int(times_repeated) - 1


else:
    print("No beat...")