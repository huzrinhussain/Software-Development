import random


hidden = 6
guess = None

while guess != hidden:
    guess = random.randrange(1, 20)
    print("wrong")
    if guess == hidden:
        print("You guessed correctly")
        break 
