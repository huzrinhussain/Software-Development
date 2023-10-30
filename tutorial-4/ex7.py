import random

doubles_count = 0

for i in range(6):
    die1 = random.randint(1, 6)

    die2 = random.randint(1, 6)

    if die1 == die2:
        doubles_count += 1

print("The number of doubles rolled is:", doubles_count)