import customtkinter as ctk
import nltk
import random
from nltk.corpus import words


# Title Screen
window1 = ctk.CTk()
window1.geometry('330x160')
window1.title('Title Screen')


# Default Difficulty
slider1Val = 3 
slider1Str = 'Normal' 

# Initializing variables
guessedLetters = []
count = 0

# Randomly selected word
allwords = words.words()
chosenWord = random.choice(allwords)
while len(chosenWord) < 3 or len(chosenWord) > 9:
	chosenWord = random.choice(allwords)

print(chosenWord)

for letter in chosenWord:
	guessedLetters.append('_')
print(guessedLetters)



# Functions 
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

def aButtonEvent():
    print("The letter selected is 'A'")
    aButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "a"
    check(guess)

def bButtonEvent():
    print("The letter selected is 'B'")
    bButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "b"
    check(guess)

def cButtonEvent():
    print("The letter selected is 'C'")
    cButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "c"
    check(guess)

def dButtonEvent():
    print("The letter selected is 'D'")
    dButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "d"
    check(guess)

def eButtonEvent():
    print("The letter selected is 'E'")
    eButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "e"
    check(guess)

def fButtonEvent():
    print("The letter selected is 'F'")
    fButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "f"
    check(guess)

def gButtonEvent():
    print("The letter selected is 'G'")
    gButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "g"
    check(guess)

def hButtonEvent():
    print("The letter selected is 'H'")
    hButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "h"
    check(guess)

def iButtonEvent():
    print("The letter selected is 'I'")
    iButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "i"
    check(guess)

def jButtonEvent():
    print("The letter selected is 'J'")
    jButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "j"
    check(guess)

def kButtonEvent():
    print("The letter selected is 'K'")
    kButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "k"
    check(guess)

def lButtonEvent():
    print("The letter selected is 'L'")
    lButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "l"
    check(guess)

def mButtonEvent():
    print("The letter selected is 'M'")
    mButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "m"
    check(guess)

def nButtonEvent():
    print("The letter selected is 'N'")
    nButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "n"
    check(guess)

def oButtonEvent():
    print("The letter selected is 'O'")
    oButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "o"
    check(guess)

def pButtonEvent():
    print("The letter selected is 'P'")
    pButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "p"
    check(guess)

def qButtonEvent():
    print("The letter selected is 'Q'")
    qButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "q"
    check(guess)

def rButtonEvent():
    print("The letter selected is 'R'")
    rButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "r"
    check(guess)

def sButtonEvent():
    print("The letter selected is 'S'")
    sButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "s"
    check(guess)

def tButtonEvent():
    print("The letter selected is 'T'")
    tButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "t"
    check(guess)

def uButtonEvent():
    print("The letter selected is 'U'")
    uButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "u"
    check(guess)

def vButtonEvent():
    print("The letter selected is 'V'")
    vButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "v"
    check(guess)

def wButtonEvent():
    print("The letter selected is 'W'")
    wButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "w"
    check(guess)

def xButtonEvent():
    print("The letter selected is 'X'")
    xButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "x"
    check(guess)

def yButtonEvent():
    print("The letter selected is 'Y'")
    yButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "y"
    check(guess)

def zButtonEvent():
    print("The letter selected is 'Z'")
    zButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    guess = "z"
    check(guess)
    
def check(guess):
	global count
	for letter in range(len(chosenWord)):
		if chosenWord[letter] == guess:
			guessedLetters[letter] = guess
			puzzleLabel.configure(text = guessedLetters)
		else: 
			count += 1
	return count

def goButtonEvent():
    global puzzleLabel
    print("The selected difficulty is:", slider1Str)
    window1.withdraw()
    window2 = ctk.CTk()
    window2.geometry('900x450')
    window2.title('Hangman')
    hangmanFrame = ctk.CTkFrame(window2,
                            fg_color = '#222222',
                            width = 550,
                            height = 450)
    hangmanFrame.place(x = 0,
                       y = 0)

    lettersFrame = ctk.CTkFrame(window2,
                            fg_color = '#555555',
                            width = 350,
                            height = 450)

    lettersFrame.place(x = 550,
                       y = 0)

    puzzleLabel = ctk.CTkLabel(lettersFrame,
    						   text = guessedLetters,
    						   font = ('Calibri',30),
    						   fg_color = '#555555',
    						   width = 350,
    						   height = 320)
    						   

    fontSize = 0 # Intializing the font size
    length = len(chosenWord)

    if length == 3:
    	fontSize = 160
    	yVal = 203
    elif length == 4:
    	fontSize = 125
    	yVal = 218
    elif length == 5:
    	fontSize = 100
    	yVal = 233
    elif length == 6:
    	fontSize = 80
    	yVal = 243
    elif length == 7:
    	fontSize = 69
    	yVal = 248
    elif length == 8:
    	fontSize = 60
    	yVal = 253
    elif length == 9:
    	fontSize = 53
    	yVal = 258
    else:
    	print("Something's wrong")

    puzzleLabel.configure(font = ('Calibri',fontSize))
    puzzleLabel.place(x = 1,
    				  y = yVal)

    global aButton
    aButton = ctk.CTkButton(lettersFrame,
                          text = "A",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = aButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    aButton.place(x = 0,
                  y = 0)

    global bButton
    bButton = ctk.CTkButton(lettersFrame,
                          text = "B",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = bButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    bButton.place(x = 50,
                  y = 0)

    global cButton
    cButton = ctk.CTkButton(lettersFrame,
                          text = "C",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = cButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    cButton.place(x = 100,
                  y = 0)

    global dButton
    dButton = ctk.CTkButton(lettersFrame,
                          text = "D",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = dButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    dButton.place(x = 150,
                  y = 0)

    global eButton
    eButton = ctk.CTkButton(lettersFrame,
                          text = "E",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = eButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    eButton.place(x = 200,
                  y = 0)

    global fButton
    fButton = ctk.CTkButton(lettersFrame,
                          text = "F",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = fButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    fButton.place(x = 250,
                  y = 0)

    global gButton
    gButton = ctk.CTkButton(lettersFrame,
                          text = "G",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = gButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    gButton.place(x = 300,
                  y = 0)

    global hButton
    hButton = ctk.CTkButton(lettersFrame,
                          text = "H",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = hButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    hButton.place(x = 0,
                  y = 50)

    global iButton
    iButton = ctk.CTkButton(lettersFrame,
                          text = "I",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = iButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    iButton.place(x = 50,
                  y = 50)

    global jButton
    jButton = ctk.CTkButton(lettersFrame,
                          text = "J",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = jButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    jButton.place(x = 100,
                  y = 50)

    global kButton
    kButton = ctk.CTkButton(lettersFrame,
                          text = "K",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = kButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    kButton.place(x = 150,
                  y = 50)

    global lButton
    lButton = ctk.CTkButton(lettersFrame,
                          text = "L",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = lButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    lButton.place(x = 200,
                  y = 50)

    global mButton
    mButton = ctk.CTkButton(lettersFrame,
                          text = "M",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = mButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    mButton.place(x = 250,
                  y = 50)

    global nButton
    nButton = ctk.CTkButton(lettersFrame,
                          text = "N",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = nButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    nButton.place(x = 300,
                  y = 50)

    global oButton
    oButton = ctk.CTkButton(lettersFrame,
                          text = "O",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = oButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    oButton.place(x = 0,
                  y = 100)

    global pButton
    pButton = ctk.CTkButton(lettersFrame,
                          text = "P",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = pButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    pButton.place(x = 50,
                  y = 100)

    global qButton
    qButton = ctk.CTkButton(lettersFrame,
                          text = "Q",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = qButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    qButton.place(x = 100,
                  y = 100)

    global rButton
    rButton = ctk.CTkButton(lettersFrame,
                          text = "R",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = rButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    rButton.place(x = 150,
                  y = 100)

    global sButton
    sButton = ctk.CTkButton(lettersFrame,
                          text = "S",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = sButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    sButton.place(x = 200,
                  y = 100)

    global tButton
    tButton = ctk.CTkButton(lettersFrame,
                          text = "T",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = tButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    tButton.place(x = 250,
                  y = 100)

    global uButton
    uButton = ctk.CTkButton(lettersFrame,
                          text = "U",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = uButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    uButton.place(x = 300,
                  y = 100)

    global vButton
    vButton = ctk.CTkButton(lettersFrame,
                          text = "V",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = vButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    vButton.place(x = 0,
                  y = 150)

    global wButton
    wButton = ctk.CTkButton(lettersFrame,
                          text = "W",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = wButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    wButton.place(x = 50,
                  y = 150)

    global xButton
    xButton = ctk.CTkButton(lettersFrame,
                          text = "X",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = xButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    xButton.place(x = 100,
                  y = 150)

    global yButton
    yButton = ctk.CTkButton(lettersFrame,
                          text = "Y",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = yButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    yButton.place(x = 150,
                  y = 150)

    global zButton
    zButton = ctk.CTkButton(lettersFrame,
                          text = "Z",
                          text_color = ('#444444', 'green'),
                          font = ('Calibri', 20),
                          fg_color = '#999999',
                          command = zButtonEvent,
                          text_color_disabled = '#555555',
                          corner_radius = 10,
                          width = 50,
                          height = 50)
    zButton.place(x = 200,
                  y = 150)


    window2.mainloop()


# Creating subsections with frames
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

# Other functional widgets
welcomeLabel = ctk.CTkLabel(welcomeFrame,
                            text = "Welcome, please select a difficulty:",
                            text_color = 'black',
                            font = ('Calibri', 20),
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
diffSlider.place(x=65,
                 y=5)

easyLabel = ctk.CTkLabel(diffFrame,
                         text="Very Easy",
                         text_color='green')
easyLabel.place(x=5,
                y=0)

hardLabel = ctk.CTkLabel(diffFrame,
                         text="Very Hard",
                         text_color='red')
hardLabel.place(x=265,
                y=0)

goButton = ctk.CTkButton(goButtonFrame,
                         text="Begin Game",
                         command=goButtonEvent,
                         fg_color='#444444',
                         width=100,
                         height=50)
goButton.place(x=0,
               y=0)

window1.mainloop()

