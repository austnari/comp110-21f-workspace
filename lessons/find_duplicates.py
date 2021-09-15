"""Finding duplicate letters in a word."""

__author__ = "730396074"

word_entered = str(input("Enter a word: "))
i = int(len(word_entered))

last_letter_number = int(len(word_entered)) - 1
test_letter_number = int(len(word_entered)) - 2

last_letter = str(word_entered[last_letter_number])
test_letter = str(word_entered[test_letter_number])

s = 0

while i > 0:

    while test_letter_number >= 0:
        print(test_letter)
        if last_letter != test_letter:
            print(last_letter)
            last_letter_number = last_letter_number - 1
            last_letter = str(word_entered[last_letter_number])
            print(last_letter)

        else:
            s = 1
        
        test_letter_number = test_letter_number - 1
        test_letter = str(word_entered[test_letter_number])
        print(test_letter)

    i = i - 1

if s == 1:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")