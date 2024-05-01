import customtkinter as ctk
import random
from PIL import Image

def aButtonEvent():
    global misses
    guess = "a"
    check(guess)
    aButton.configure(state = 'disabled',
    				  fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()

def bButtonEvent():
    global misses
    guess = "b"
    check(guess)
    bButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()

def cButtonEvent():
    global misses
    guess = "c"
    check(guess)
    cButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()

def dButtonEvent():
    global misses
    guess = "d"
    check(guess)
    dButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def eButtonEvent():
    global misses
    guess = "e"
    check(guess)
    eButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def fButtonEvent():
    global misses
    guess = "f"
    check(guess)
    fButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()

def gButtonEvent():
    global misses
    guess = "g"
    check(guess)
    gButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()

def hButtonEvent():
    global misses
    guess = "h"
    check(guess)
    hButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def iButtonEvent():
    global misses
    guess = "i"
    check(guess)
    iButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def jButtonEvent():
    global misses
    guess = "j"
    check(guess)
    jButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def kButtonEvent():
    global misses
    guess = "k"
    check(guess)
    kButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def lButtonEvent():
    global misses
    guess = "l"
    check(guess)
    lButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def mButtonEvent():
    global misses
    guess = "m"
    check(guess)
    mButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def nButtonEvent():
    global misses
    guess = "n"
    check(guess)
    nButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def oButtonEvent():
    global misses
    guess = "o"
    check(guess)
    oButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def pButtonEvent():
    global misses
    guess = "p"
    check(guess)
    pButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def qButtonEvent():
    global misses
    guess = "q"
    check(guess)
    qButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def rButtonEvent():
    global misses
    guess = "r"
    check(guess)
    rButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def sButtonEvent():
    global misses
    guess = "s"
    check(guess)
    sButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def tButtonEvent():
    global misses
    guess = "t"
    check(guess)
    tButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def uButtonEvent():
    global misses
    guess = "u"
    check(guess)
    uButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def vButtonEvent():
    global misses
    guess = "v"
    check(guess)
    vButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def wButtonEvent():
    global misses
    guess = "w"
    check(guess)
    wButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def xButtonEvent():
    global misses
    guess = "x"
    check(guess)
    xButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def yButtonEvent():
    global misses
    guess = "y"
    check(guess)
    yButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def zButtonEvent():
    global misses
    guess = "z"
    check(guess)
    zButton.configure(state = 'disabled',
                      fg_color = '#555555')
    if guess not in chosenWord:
        misses += 1
        build()
        
def check(guess):
	global count1
	for letter in range(len(chosenWord)):
		if chosenWord[letter] == guess:
			guessedLetters[letter] = guess
			puzzleLabel.configure(text = guessedLetters)
		else: 
			count1 += 1
	return count1

def gameover():
    aButtonEvent()
    bButtonEvent()
    cButtonEvent()
    dButtonEvent()
    eButtonEvent()
    fButtonEvent()
    gButtonEvent()
    hButtonEvent()
    iButtonEvent()
    jButtonEvent()
    kButtonEvent()
    lButtonEvent()
    mButtonEvent()
    nButtonEvent()
    oButtonEvent()
    pButtonEvent()
    qButtonEvent()
    rButtonEvent()
    sButtonEvent()
    tButtonEvent()
    uButtonEvent()
    vButtonEvent()
    wButtonEvent()
    xButtonEvent()
    yButtonEvent()
    zButtonEvent()

def win():
    if '_' not in chosenWord:
        print("You won!")
        gameover()

def build():
    if misses == 1:
        headImage = ctk.CTkImage(dark_image = Image.open("/Users/gallonguy/Desktop/HangmanParts/hangmanHead.PPM"),
                                 size = (80, 80))
        headLabel = ctk.CTkLabel(hangmanFrame,
                                 image = headImage,
                                 text = " ")
        headLabel.place(x = 243,
                        y = 92)
    elif misses == 2:
        torsoImage = ctk.CTkImage(dark_image = Image.open("/Users/gallonguy/Desktop/HangmanParts/hangmanTorso.PPM"),
                                 size = (7, 120))
        torsoLabel = ctk.CTkLabel(hangmanFrame,
                                 image = torsoImage,
                                 text = " ")
        torsoLabel.place(x = 280,
                         y = 171)
    elif misses == 3:
        leg1Image = ctk.CTkImage(dark_image = Image.open("/Users/gallonguy/Desktop/HangmanParts/hangmanLeg1.PPM"),
                                 size = (43, 80))
        leg1Label = ctk.CTkLabel(hangmanFrame,
                                 image = leg1Image,
                                 text = " ")
        leg1Label.place(x = 242,
                        y = 289)
    elif misses == 4:
        leg2Image = ctk.CTkImage(dark_image = Image.open("/Users/gallonguy/Desktop/HangmanParts/hangmanLeg2.PPM"),
                                 size = (43, 80))
        leg2Label = ctk.CTkLabel(hangmanFrame,
                                 image = leg2Image,
                                 text = " ")
        leg2Label.place(x = 282,
                        y = 289)
    elif misses == 5:
        arm1Image = ctk.CTkImage(dark_image = Image.open("/Users/gallonguy/Desktop/HangmanParts/hangmanArm1.PPM"),
                                 size = (80, 40))
        arm1Label = ctk.CTkLabel(hangmanFrame,
                                 image = arm1Image,
                                 text = " ")
        arm1Label.place(x = 203,
                        y = 175)

        torsoImage = ctk.CTkImage(dark_image = Image.open("/Users/gallonguy/Desktop/HangmanParts/hangmanTorso.PPM"),
                                 size = (7, 120))
        torsoLabel = ctk.CTkLabel(hangmanFrame,
                                 image = torsoImage,
                                 text = " ")
        torsoLabel.place(x = 280,
                        y = 171)
    elif misses == 6:
        arm2Image = ctk.CTkImage(dark_image = Image.open("/Users/gallonguy/Desktop/HangmanParts/hangmanArm2.PPM"),
                                 size = (80, 40))
        arm2Label = ctk.CTkLabel(hangmanFrame,
                                 image = arm2Image,
                                 text = " ")
        arm2Label.place(x = 283,
                        y = 175)

        torsoImage = ctk.CTkImage(dark_image = Image.open("/Users/gallonguy/Desktop/HangmanParts/hangmanTorso.PPM"),
                                 size = (7, 120))
        torsoLabel = ctk.CTkLabel(hangmanFrame,
                                 image = torsoImage,
                                 text = " ")
        torsoLabel.place(x = 280,
                         y = 171)
        print(f"You lose!\nThe word was: {chosenWord}!")
        gameover()

window2 = ctk.CTk()
window2.geometry('900x450')
window2.title('Hangman')

# Initializing variables
guessedLetters = []
count1 = 0
misses = 0
fontSize = 0

# Randomly selected word
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

while len(chosenWord) < 3 or len(chosenWord) > 9:
    chosenWord = random.choice(wordList)

for letter in chosenWord:
    guessedLetters.append('_')

# Other widgets
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

# Hangman functionality

structureImage = ctk.CTkImage(dark_image = Image.open("/Users/gallonguy/Desktop/HangmanParts/hangmanStructure.PPM"),
                              size = (550, 450))
structureLabel = ctk.CTkLabel(hangmanFrame,
                              image = structureImage,
                              text = " ")
structureLabel.place(x = 0,
                     y = 0)

if len(chosenWord) == 3:
    fontSize = 160
    yVal = 203
elif len(chosenWord) == 4:
    fontSize = 125
    yVal = 218
elif len(chosenWord) == 5:
    fontSize = 100
    yVal = 233
elif len(chosenWord) == 6:
    fontSize = 80
    yVal = 243
elif len(chosenWord) == 7:
    fontSize = 69
    yVal = 248
elif len(chosenWord) == 8:
    fontSize = 60
    yVal = 253
elif len(chosenWord) == 9:
    fontSize = 53
    yVal = 258
else:
    print("Something's wrong")

puzzleLabel.configure(font = ('Calibri',fontSize))
puzzleLabel.place(x = 1,
    			  y = yVal)

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