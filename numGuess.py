# from random import randint
import random

n=random.randint(0,100)
a=-1

guesses=1
while(a!=n):
    a= int(input("Guess a number between 0 to 100: "))
    if(a>n):
        print("Guess lower number please..")
        guesses+=1
    else:
        print("Guess heigher number please...")
        guesses+=1

print(f"You have guessed the correct number {n} in {guesses} attempt..")
