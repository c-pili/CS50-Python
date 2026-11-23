import sys

from emoji import emojize

emoji = input("Input: ")
try:
    print(emojize(emoji))
except:
    print("Invalid usage")
    sys.exit(1)
