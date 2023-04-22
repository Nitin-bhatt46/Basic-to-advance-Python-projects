
import random

n=random.randrange(2,100)
guess= int (input("enter any number between 2 to 100 : "))

while n != guess:
    if guess < n:
        print("too low")
        guess = int(input("Enter number again :"))
    elif guess> n:
        print("too high")
        guess = (int(input("Enter number again :")))
    else:
        break
print("You guessed it right !!")