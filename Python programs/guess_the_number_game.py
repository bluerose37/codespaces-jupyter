import random
secret = random.randint(1, 50)

while True:
    guess = int(input("Guess a number between 1-50: "))
    if guess == secret:
        print("You got it! 🎉")
        break
    elif guess < secret:
        print("Low, try again")
    else:
        print("High, try again")