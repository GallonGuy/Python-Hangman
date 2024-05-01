# Hangman Project


import random
import nltk

# nltk.download('words')
from nltk.corpus import words

# The 'words' corpus is now a list of English words.
allwords = words.words()

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessedLetters = []
correctLetters = []
incorrectLetters = []
numBodyParts = 0
difficultyScale = 0


# Preparing the difficulty

difficultyScale = int(input("Select a difficulty (number of letters you may guess)\n1 is the easiest, and 5 is the hardest (integers only)"))
while difficultyScale not in [1,2,3,4,5]:
	print("That's no good, you need to select a difficulty from 1 to 5 where 1 is the easiest and 5 is the hardest")
	difficultyScale = int(input("The difficulty must be an integer between 1 and 5 (1 is easiest, 5 is hardest)."))

if difficultyScale == 1:
	numberOfGuesses = 14
elif difficultyScale == 2:
	numberOfGuesses = 12
elif difficultyScale == 3:
	numberOfGuesses = 10
elif difficultyScale == 2:
	numberOfGuesses = 8
elif difficultyScale == 1:
	numberOfGuesses = 6
else:
	print("There's an error in the difficultyScale")


# The game

chosenWord = random.choice(allwords)
while len(chosenWord) < 3 or len(chosenWord) > 9:
	chosenWord = random.choice(allwords)

for letter in chosenWord:
	guessedLetters.append('_')

print(guessedLetters,"\n")


# Guess a letter

def guessALetter():
    guess = input("Guess a letter, please: ")
    while guess not in alphabet:
    	guess = input("Guess one letter, please: ")

    while guess in incorrectLetters or guess in correctLetters:
        print("Sorry, you need to choose another letter\nhere's a list of the letters you've already chosen: %s." %(correctLetters + incorrectLetters))
        guess = input("Guess a letter, please: ")
    return guess


# Checking if the letter is there or not

def checkIfItsThere():
	guess = guessALetter()

	for i in range(len(chosenWord)):
	    if chosenWord[i] == guess:
	        guessedLetters[i] = guess
	if guess in chosenWord:
		correctLetters.append(guess)

	if guess not in chosenWord:
	    	print("Sorry, the letter %s isn't in there!" %guess)
	    	incorrectLetters.append(guess)

	print(str(guessedLetters)+"\n")
checkIfItsThere()


def playGame():
	while len(incorrectLetters) < numberOfGuesses and "_" in guessedLetters:
		checkIfItsThere()

playGame()

if len(incorrectLetters) == numberOfGuesses:
	print("You lost... the word was:",chosenWord)
elif "_" not in guessedLetters:
	print("You guessed the word!")
	print(chosenWord.capitalize())