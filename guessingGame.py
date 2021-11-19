import random

# Set number of guesses to 0
# Set user input to default 0
# Get input for bottom of range
# Get input for top of range
# Check if bottom of range is a number
# if bottom of range is less than or equal to 0
# print Please type a number larger than 0 next time
# else print Please type a number next time
# Check if top of range is a number
# IF top of range is less than or equal to bottom of range
# print please type a number larger than bottom of range next time
# IF top of range is not a number
# print Please type a number next time
numberOfGuesses = 0
userGuess = 0
bottomOfRange = input("Type a number: ")
topOfRange = input("Type a number: ")

if bottomOfRange.isdigit():
    bottomOfRange = int(bottomOfRange)

    if bottomOfRange <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

if topOfRange.isdigit():
    topOfRange = int(topOfRange)

    if topOfRange <= bottomOfRange:
        print("Please type a number larger than", bottomOfRange, "time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
randomNum = random.randint(bottomOfRange, topOfRange)
# WHILE the random number is not equal to random number
# Take number of guesses and add one for every guess made
# Get user input for a number that needs to be guessed
# Check if user entered a number
# IF user entered number continue
# else
# print please type a number next time
# IF the user guessed a number less than the bottom range 
# print Please type a number in the ranges selected
# ELIF user guessed a number greater than top of range
# print Please type a number in the ranges selected
# ELIF the user guessed greater than the generated random number
# print The number is lower than the guessed number
# ELIF IF the user guessed lower than than generated random number
# print The number is higher than the guessed number
# ELSE
# The user guessed number is equal to the generated random number break the WHILE loop
while userGuess != randomNum:
    numberOfGuesses += 1
    userGuess = input("Make a guess: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please type a number next time.")
        continue
    if userGuess < bottomOfRange:
        print("Please type a number in the ranges selected")
    elif userGuess > topOfRange:
        print("Please type a number in the ranges selected")
    elif userGuess > randomNum:
        print("The number is lower than", str(userGuess) + '.', "Try again.")
    elif userGuess < randomNum:
        print("The number is higher than", str(userGuess) + '.', "Try again.")
    else:
        break
print("You have guessed the right number!!!")
print("It took you", numberOfGuesses, "guesses")
