# Write a Python program to guess a number between 1 to 9.
print("******************************")
print("Please guess a number between 1 and 10: ")
guess = int(input())
if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:  # guess must be greater than 5
        print("Please guess lower")
        guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly.")
else:
    print("you got it first time")
