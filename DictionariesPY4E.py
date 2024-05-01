# Write a program to read through the mbox-short.txt and figure out who has sent 
# the greatest number of mail messages. The program looks for "From" lines and takes
# the second word of those liens as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is 
# produced, the program reads through the dictionary using a maximum loops to find
# the most prolific committer.

file = 'mbox-short.txt'
fhand = open(file)
myDict = {}
myList = []

for line in fhand:
	if len(line) < 2 or line.startswith("From ") != True:
		continue
	else:
		line = line.rstrip()
		line = line.split()
		word = line[1]
		myList.append(word)

for word in myList:
	myDict[word] = myDict.get(word,0) + 1

minVal = min((myDict.values()))

for key,val in myDict.items():
	if val == minVal:
		print(key,val)