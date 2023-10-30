
hidden = 6
guess = range(1,20)

while guess != hidden:
    guess = int(input("Enter a guess: "))
    if guess == hidden:
        print("You guessed correctly")
        break