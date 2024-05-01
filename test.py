'''
x = [1,2,3]
print(x)
x.pop(1)
x.insert(1,'thing')
print(x)

y = ['a', '9', '*', 'L', '49999','4.9','4','$', 'Z','Gallstone','Gaz']
y.sort()
print(y)

abc = "With three words"
z = "abcdef"
str = abc.split()
print(str)
for i in str:
	print(i)
print(z.find('f'))

import customtkinter as ctk

# Create root window
root = ctk.CTk()
root.withdraw()  # Hide root window

# Title screen and difficulty selection
window1 = ctk.CTkToplevel(root)
window1.geometry('330x160')
window1.title('Title Screen')

def goButtonEvent():
    print("The selected difficulty is:", slider1Str)
    window1.withdraw()  # Hide window1 instead of destroying it
    create_window2()

def create_window2():
    window2 = ctk.Toplevel(root)
    window2.geometry('1000x600')
    window2.title('Hangman')

def slider1Event(diffSlider):
    global slider1Str
    slider1Val = diffSlider
    if slider1Val == 1:
        slider1Str = 'Very easy'
    elif slider1Val == 2:
        slider1Str = 'Easy'
    elif slider1Val == 3:
        slider1Str = 'Normal'
    elif slider1Val == 4:
        slider1Str = 'Hard'
    elif slider1Val == 5:
        slider1Str = 'Very hard'
    return slider1Str

# Creating the widgets in the window

welcomeFrame = ctk.CTkFrame(window1,
							width = 330,
							height = 57,
							fg_color = '#666666')

welcomeFrame.place(x = 0,
				   y = 2)

diffFrame = ctk.CTkFrame(window1,
						 width = 330,
						 height = 30,
						 fg_color = '#555555')
diffFrame.place(x = 0,
				y = 60)

goButtonFrame = ctk.CTkFrame(window1,
							 width = 100,
							 height = 50)
goButtonFrame.place(x = 115,
					y = 100)

welcomeLabel = ctk.CTkLabel(welcomeFrame,
							text = "Welcome, please select a difficulty:",
							text_color = 'black',
							font = ('Calibri',20),
							width = 330,
							height = 57)
welcomeLabel.place(x = 0,
				   y = 0)

diffSlider = ctk.CTkSlider(diffFrame,
                            from_ = 1,
                            to = 5,
                            number_of_steps = 4,
                            width = 200,
                            height = 20,
                            command = slider1Event)
diffSlider.place(x = 65,
				 y = 5)

easyLabel = ctk.CTkLabel(diffFrame,
							text = "Very Easy",
							text_color = 'green')
easyLabel.place(x = 5,
				y = 0)

hardLabel = ctk.CTkLabel(diffFrame,
						text = "Very Hard",
						text_color = 'red')
hardLabel.place(x = 265,
				y = 0)

goButton = ctk.CTkButton(goButtonFrame,
                        text = "Begin Game",
                        command = goButtonEvent,
                        fg_color = '#444444',
                        width = 100,
                        height = 50)
goButton.place(x = 0,
			   y = 0)

window1.mainloop()

hangmanFrame = ctk.CTkFrame(window2,
							fg_color = '#222222',
							width = 550,
							height = 450)
hangmanFrame.place(x = 0,
				   y = 0)

lettersFrame = ctk.CTkFrame(window2,
						    fg_color = '#555555',
						    width = 450,
						    height = 450)
lettersFrame.place(x = 550,
				   y = 0)

puzzleFrame = ctk.CTkFrame(window2,
						   fg_color = '#888888',
						   width = 1000,
						   height = 150)

puzzleFrame.place(x = 0,
				  y = 450)


window2.mainloop()

print(slider1Str)




fname = 'romeo_text_file.txt'
fhand = open(fname)
ourList = []
goal = []
for line in fhand:
	if len(line) < 2:
		continue
	else:
		newline = line.rstrip()
		newerline = newline.split()
		for word in newerline:
			if word in goal:
				continue
			else:
				goal.append(word)
				goal.sort()

print(str(goal))


file = 'mbox-short.txt'
fhand = open(file)
count = 0
for line in fhand:
	if len(line) < 2:
		continue
	elif line.startswith('From:') == True :
		continue
	elif line.startswith('From'):
		newline = line.rstrip()
		newerline = newline.split()
		print(newerline[1])
		count += 1

print(f"There were {count} lines in the file with From as the first word")


myDict = {}
myDict['A'] = 1
myDict['B'] = 1
myDict['A'] += 1
print(f"The dictionary is: {myDict}")


counts = {}
line = input('Enter a line of text')
words = line.split()
print(f"The words are: {words}")
for word in words:
	counts[word] = counts.get(word,0) + 1
print(f"The counts are: {counts}")

fhand = open('mbox-short.txt')
counts = {}
myList = []
for line in fhand:
	if len(line) < 2 or line.startswith("From ") == False:
		continue
	else:
		line = line.rstrip()
		line = line.split()
		for word in line:
			counts[word] = counts.get(word,0) + 1
for (key,val) in counts.items():
	newTuple = (val,key)
	myList.append(newTuple)
myList = sorted(myList, reverse = True)
for (val,key) in myList[:10]:
	print(key,val)

fhand = open('mbox-short.txt')
myList = []
yourList = []
myDict = {}
maxVal = 0
secondMax = 0
secondKey = ''
for line in fhand:
	line = line.rstrip()
	line = line.split()
	if len(line) < 2:
		continue
	elif 'From' in line:
		myList.append(line[line.index('From') + 1])
	elif 'FROM' in line:
		myList.append(line[line.index('FROM') + 1])
	elif 'from' in line:
		if line[line.index('from') + 1] == 'the':
			continue
		else:
			myList.append(line[line.index('from') + 1])

for word in myList:
	myDict[word] = myDict.get(word,0) + 1

for key,val in myDict.items():
	if val > maxVal:
		maxVal = val
	else:
		continue

for key,val in myDict.items():
	if val == maxVal:
		continue
	elif val > secondMax:
		secondMax = val
		secondKey = key
	else: continue
print(f"The second most used name is: {secondKey}, at {secondMax} uses!")


file = 'mbox-short.txt' # File name
fhand = open(file) # File handle to read the .txt file
myDict = {} # Hollowing out a fresh dictionary for later

for line in fhand: # Goes line by line
	if len(line) < 2 or line.startswith('From ') == False: # Guardian and only sorts lines we want to read with startswith() statement
		continue # continues if we grab the wrong line
	else:
		line = line.rstrip() # removing \newlines
		line = line.split() # splitting words apart
		time = line[5] # finding the hours:min:sec times the messages were sent
		hour = time[0:2] # reducing hours:mins:seconds to hours
		myDict[hour] = myDict.get(hour,0) + 1 # counting the amount of times each hour is seen

for key,val in sorted(myDict.items()): # Sorts hours chronologically and applies the count to each hour seen
	print(key,val) # prints "{hours} {count}"
'''
'''
import re

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
'''
import re

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.findall('From:', line):
        print(line)


	


	