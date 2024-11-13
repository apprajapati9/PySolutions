import sys
import random

print("enter your name")
name = input()

try:
    for i in name:
        if i.isnumeric():
            raise TypeError("Numbers not allowed in name")
except TypeError as e:
    print(e)
    sys.exit()

print("your name is " + name)
answer = random.randint(1,20)
guesses = 0
guess = -1
print("Guess number between 1 to 20")
while guess != answer:
    guess = int(input())
    guesses+=1
    if guess > answer:
        print("try lower")
    else:
        print("try higher")

print("you took {} guesses".format(guesses))
