import random

file = 'fairwords.txt'
fhand = open(file)
wordList = []

for line in fhand:
	newline = line.rstrip()
	group = newline.split()
	for word in group:
		word.split()
		wordList.append(word)


chosenWord = random.choice(wordList)
print(chosenWord)
