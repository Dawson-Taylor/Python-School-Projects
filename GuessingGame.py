import random

# Generate a random number between one and ten
# Set number of guesses to 0
# Set user input to default 0
topOfRange = input("Type a number: ")

if topOfRange.isdigit():
    topOfRange = int(topOfRange)

    if topOfRange <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
randomNum = random.randint(0, topOfRange)
numberOfGuesses = 0
userGuess = 0

# WHILE the random number is not equal to random number
# Take number of guesses and add one for every guess made
# Get user input for a number that needs to be guessed
# Check if user entered a number
# IF user entered number continue
# else
# print please type a number next time
# IF the user guessed greater than the generated random number
# print The number is lower than the guessed number
# ELSE IF the user guessed lower than than generated random number
# print The number is higher than the guessed number
# ELSE
# The user guessed number is equal to the generated random number break the WHILE loop
while userGuess != randomNum:
    numberOfGuesses += 1
    userGuess = input("Guess a number between 1 and 10: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please type a number next time.")
        continue
    if userGuess > randomNum:
        print("The number is lower than", str(userGuess) + '.', "Try again.")
    elif userGuess < randomNum:
        print("The number is higher than", str(userGuess) + '.', "Try again.")
    else:
        break
print("You have guessed the right number!!!")
print("It took you", numberOfGuesses, "guesses")
