"""Counting letters in a string."""

__author__ = "730396074"

letter = str(input("What letter do you want to search for?: "))
word_entered = str(input("Enter a word: "))
i = int(len(word_entered))
number = int(0)

while i > 0:
    if word_entered[i - 1] == letter:
        number = number + 1
    i = i - 1
print("Count: " + str(number))