import random


hidden = 6
guess = None

while guess != hidden:
    guess = random.randrange(1, 20)
    if guess < hidden:
        print("You guessed too low")
    elif guess > hidden:
        print("You guessed too high")
    else:
        print("You guessed correctly")
        break 
