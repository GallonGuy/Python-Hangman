""" Learn the Basics category of https://www.learnpython.org/
1. Hello, World!
2. Variables and Types
3. Lists
4. Basic Operators
5. String Formatting
6. Basic String Operations
7. Conditions
8. Loops
9. Functions
10. Class and Objects
11. Dictionaries
12. Modules and Packages
"""

# 1. Hello, World:
# Use the "print" function to print the line "Hello, World!".
print("Hello, World!")

# 2. Variables and Types:

x = 7
print(x)
xfloat = float(x)
print(xfloat)
xint = int(xfloat)
print(xint)
xstr = str(xint)
print(xstr)

a, b = 3, 4
print(a,b,b)

# The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello".
# The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.

mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# 3. Lists

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

# Indexing lists starts at 0
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
print("The length of 'mylist' is: %s" %len(mylist))
print("'mylist' looks like this: %s" %mylist)

# In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method.
# You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
# You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator [].
# Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
print("The numbers list is now: %s, while the names list is now: %s, and the strings list is now: %s" % (numbers, names, strings))

# 4. Basic Operators:

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

Concatenating_Hello_World = "hello" + " " + "world"
print(Concatenating_Hello_World)

Lots_Of_Hellos = "hello " * 10
print(Lots_Of_Hellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

# The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively.
# You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# 5. String Formatting

# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

# 6. Basic String Operations

Part_6_astring = "Hello world!"
print(len(Part_6_astring)) # This prints 12 because spaces and punctuation count in the string length.
print(Part_6_astring.index("o")) # This method only recognizes the first and indexing starts at 0.
print(Part_6_astring.count("l")) # This counts the number of times "l" shows up un "Hello world!"
print(Part_6_astring[3:7]) # This grabs the 4th through 8th character of the string
print(Part_6_astring[3:7:3]) # This grabs the 4th through 8th character of the string and then skips two characters (o and space) [start:stop:single step]
print(Part_6_astring[::-1]) # This reverses the string
print(Part_6_astring.upper())
print(Part_6_astring.lower())
print(Part_6_astring.startswith("Hello")) # Results in boolean true
print(Part_6_astring.endswith("chocolate")) # Results in boolean false
afewwords = Part_6_astring.split(" ")
print(Part_6_astring)
print(afewwords)

# Try to fix the code to print out the correct information by changing the string.

s = "Strip that handsome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# 7. Conditions
Part_7_x = 2
print(Part_7_x == 2) # prints out True
print(Part_7_x == 3) # prints out False
print(Part_7_x < 3) # prints out True

Part_7_name = "John"
Part_7_age = 23
if Part_7_name == "John" and Part_7_age == 23:
    print("Your name is John, and you are also 23 years old.")

if Part_7_name == "John" or Part_7_name == "Rick":
    print("Your name is either John or Rick.")
if Part_7_name in ["John","Rick"]:
	print("Your name is either John or Rick.")
statement = False
another_statement = True
if statement is True:
    print("Apples")
    pass
elif another_statement is True: # else if
    print("Bananas")
    pass
else:
    print("Cherries")
    pass

Part_7_a = [1,2,3]
Part_7_b = [1,2,3]
print(Part_7_a == Part_7_b)
print(Part_7_a is Part_7_b)

print(not False) # Prints out True
print((not False) == (False)) # Prints out False

# Change the variables in the first section, so that each if statement resolves as True.

# change this code
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# 8. Loops

Part_8_primes = [2,3,5,7]
for Part_8_x in Part_8_primes:
	print(Part_8_x)

for Part_8_Temp in range(3,25,2): # (Initial value,)
	print(Part_8_Temp)

Part_8_y = 0
Part_8_i = 0
while Part_8_i < 10:
	Part_8_i += 1
	Part_8_y += 2
print("After %s iterations, y is equal to: %s" %(Part_8_i, Part_8_y))

Part_8_Count = 0
while Part_8_Count < 5:
	print(Part_8_Count)
	Part_8_Count += 1
	if Part_8_Count >= 5:
		break

for Part_8_z in range(10):
	if Part_8_z % 2 == 0:
		continue
	print(Part_8_z)

Part_8_number = 21433

while True:
    is_prime = True

    for i in range(2, int(Part_8_number ** 0.5) + 1): # The computer iterates from 2 to the square root of the number to see if any of the values of i divide evenly. If they do, the number isn't prime
        if Part_8_number % i == 0:
            is_prime = False
            break # If the number is not prime, it skips that number and moves to the next

    if is_prime: #If the number is prime, the code doesn't break, allowing for the number to be printed
        print(Part_8_number)

    Part_8_number += 1

    if Part_8_number > 21500: # This break stops the loop when the number exceeds
        break

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    
    elif (number % 2) == 0:
        print(number)

# 9. Functions

# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
Part_9_x = sum_two_numbers(1,2)

# In this exercise you'll use an existing function, and while adding your own to create a fully functional program.
# Add a function named list_benefits() that returns the following list of strings:
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string
# and ending with the string: " is a benefit of functions!"
# Run and see all the functions work together!

# Modify this function to return a list of strings as defined above
def list_benefits(): # This is the helper function that holds the subject of each sentence
    return ["More organized code","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]

def build_sentence(benefit): # This is the helper function that builds the framework of each sentence
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions(): # This function is our main function that we'll call... it itself calls the two helper functions
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions() # Calling the main function

# 10. Classes and Objects

# Holy smokes, Space Cowboy, this is a doosy!

# So objects will have class properties, which are its attributes that distinguish it.
# For instance, a set of playing cards has the class "Card", and an object of that class is the Queen_Of_Spades.
# It is an object of the class because the class "Card" defines its attributes.
# The card has "attributes", like rank and suit. We can creat instances of objects for a specific class after we initialize the class:

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

def create_deck():
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    deck = []
    for suit in suits:
        for rank in ranks:
            card = Card(rank, suit)
            deck.append(card)

    return deck

# Create the deck of cards
deck_of_cards = create_deck()

def getsuit(Card):
	return card.suits

# We have a class defined for vehicles.
# Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
# define the Vehicle class

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

# 11. Dictionaries

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
del phonebook["Jack"] # or phonebook.pop("John")
for name,number in phonebook.items():
    print("Phone number of %s is %d" %(name,number))
print(phonebook)

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook["Jake"] = 938273443
print(phonebook)

# 13. Modules and Packages






