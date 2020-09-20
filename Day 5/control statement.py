# days = int(input("How may days in August?"))

# if days == 31:
#     print("You got it")


# print("Congrats!")


# days = int(input("How may days in August?"))

# if days == 31:
#     print("You got it")
# else:
#     print("Wrong answer")


# print("Congrats!")

# score = int(input("What is your exam score?"))

# if score > 80:
#     print("Congrats You Clear")
# elif score < 80 and score > 60:
#     print("Congrats you cleared but stil you need work hard")
# else:
#     print("Sorry try next time")


# print("Please guess a number between  1 and 10: ")
# guess = int(input())

# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correclty")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correclty")
# else:
#     print("You got it first time")

print("If else ".center(50, '*'))

print("Please guess a number between  1 and 10: ")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == 5:
         print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correclty")
else:
    print("You got it first time")
