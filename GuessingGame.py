import random


# Generate a random number between one and ten
# Set number of guesses to 0 
randomNum = random.randint(0, 10)
numberOfGuesses = 0 

# WHILE the random number is not equal to random number 
  # Get user input for a number that needs to be guessed
  # IF the user guessed greater than the generated random number
    # print The number is lower than the guessed number
  # ELSE IF the user guessed lower than than generated random number
    # print The number is higher than the guessed number
  # ELSE 
    # The user guessed number is not lower than or greater than the generated random number break the IF loop
while userGuess != randomNum
  numberOfGuesses += 1
  userGuess = int(input("Guess a number between 1 and 10: "))
  if userGuess > randomNum:
    print("The number is lower than", userGuess + '.', "Try again.")
    continue
  elif userGuess < randomNum:
    print("The number is higher than", userGuess + '.', "Try again.")
    continue
  else:
    break
print("You have guessed the right number!!!")
print("It took you this many", numberOfGuesses, "guesses")
