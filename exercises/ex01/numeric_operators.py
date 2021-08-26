"""Practicing numberic operators"""

__author__ = "730396074"

Left: int = int((input("What is your number for the left-hand side? ")))
Right: int = int((input("What is your number for the right-hand side? ")))

print("Left-hand side: " + str(Left))
print("Right-hand side: " + str(Right))

print(str(int(Left)) + " ** " + str(int(Right)) + " is " + str(int(Left ** Right)))
print(str(int(Left)) + " / " + str(int(Right)) + " is " + str(float(Left / Right)))
print(str(int(Left)) + " // " + str(int(Right)) + " is " + str(int(Left // Right)))
print(str(int(Left)) + " % " + str(int(Right)) + " is " + str(int(Left % Right)))