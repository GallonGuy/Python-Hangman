"""
 First off, as an introduction to counting cards in blackjack:
1. Cards are assigned a value: 1, 0, or -1. These values correspond to the numerical value of the card pulled, where the larger the number of "points" the card has, the higher the "value".
This will be quantitatively defined later in the program
2. The consequence of pulling a new card from a shuffled deck is that the deck no longer has that card, and now has a smaller number of cards.
This means that if we pull an ace from a freshly shuffled deck, the likelyhood of pulling an ace out of the deck goes from 4/52 to 3/51.
Obviously if this continues and the first four pulled cards are aces, there is a 0/48 chance that we can pull an ace from the deck.
This means there is no hope of 21 in the first two cards, and likewise there is no chance the dealer will either.
3. This can be extrapolated to determine your chances of getting a desirable card (a card that brings you closer to 21 without going over).
For instance if all of 2's, 3's, 4's, 5's, and 6's are pulled, and you start with two sevens in your hand, the only way you don't bust is getting one of the two sevens or aces.
This constitutes 6/32 or roughly a 30% chance of not busting, and also means that the dealer is likely to be in a similar predicament so it's in your best interest to stay
4. The dealer is forced to take additional cards (hits) at or below 16, and must stay above 16.
This can be used in your advantage since the dealer's choices can't be influenced by the count of the cards, while yours can.
This advantage is the genesis of why counting cards is lucrative and why people get beat up or lose their lives in Vegas.

Throughout this program, I'll explain the code in depth such that anyone can see exactly what the program is doing and follow the logic.
"""

# Part 1

# Let us begin by addressing a problem with the whole deck of cards. The program won't be visualizing each card according to its suit and points (number on the card).
# In order for the program to understand what we mean, we'll define a dictionary that "maps" (assigns) each card with a numerical value so when we search for a random card,
# the program will be able to give us a random card and not some nonsense string of random letters and symbols.
# The number to the left of the card's identity (name) is the "identity number" which is basically the card's name from the computer's perspective.

Card_Names = {
1: "two of hearts",
2: "three of hearts",
3: "four of hearts",
4: "five of hearts",
5: "six of hearts",
6: "seven of hearts",
7: "eight of hearts",
8: "nine of hearts",
9: "ten of hearts",
10: "jack of hearts",
11: "queen of hearts",
12: "king of hearts",
13: "ace of hearts",
14: "two of diamonds",
15: "three of diamonds",
16: "four of diamonds",
17: "five of diamonds",
18: "six of diamonds",
19: "seven of diamonds",
20: "eight of diamonds",
21: "nine of diamonds",
22: "ten of diamonds",
23: "jack of diamonds",
24: "queen of diamonds",
25: "king of diamonds",
26: "ace of diamonds",
27: "two of spades",
28: "three of spades",
29: "four of spades",
30: "five of spades",
31: "six of spades",
32: "seven of spades",
33: "eight of spades",
34: "nine of spades",
35: "ten of spades",
36: "jack of spades",
37: "queen of spades",
38: "king of spades",
39: "ace of spades",
40: "two of clubs",
41: "three of clubs",
42: "four of clubs",
43: "five of clubs",
44: "six of clubs",
45: "seven of clubs",
46: "eight of clubs",
47: "nine of clubs",
48: "ten of clubs",
49: "jack of clubs",
50: "queen of clubs",
51: "king of clubs",
52: "ace of clubs"
}

# pop(Card_Names(random.randint()))
# Now, let's discuss the basic card counting rules:
# Any suit of 2,3,4,5, or 6 are all considered a +1 count
# Any suit of 7,8,9 do not affect the count
# Any 10, jack, queen, king, or ace are all considered a -1 count
# This "count score" says that if we roll low numbered cards, the likelihood of drawing a higher card (like a face card) increases since the chance of pulling that low card decreases
# This principle is the same for high cards such as those which have a "number" of 10 or 11 (face cards or aces) since the chances of grabbing those cards decreases.
# The general idea is that the higher the "count", the more you'd like to bet.
# There is an absolutely frightening amount of literature explaining the math behind counting cards but suffice to say the higher the count the more you want to bet.
# The logic has to do with the high likelyhood of the dealer busting when the count is high do to her forced gameplay since the casino doesn't like dealers having free will.

# The first library assigned the identity number to the identity like so: (identity number:identity), but this time we'll assign the identity number to the count
# The format will be like this: (identity number:count). This will be the last of the monotonous libraries.
Card_Counts = {
# The first line represents all of the cards that will increase your count by 1:
    1:1, 2:1, 3:1, 4:1, 5:1, 14:1, 15:1, 16:1, 17:1, 18:1, 27:1, 28:1, 29:1, 30:1, 31:1, 40:1, 41:1, 42:1, 43:1, 44:1,
# The second line represents all of the cards that will not affect your count:
    6:0, 7:0, 8:0, 19:0, 20:0, 21: 0, 32:0, 33:0, 34:0, 45:0, 46:0, 47:0, 
# The last line represents all of the cards that will decrease your count by 1:
    9:-1, 10:-1, 11:-1, 12:-1, 13:-1, 22:-1, 23:-1, 24:-1, 25:-1, 26:-1, 35:-1, 36:-1, 37:-1, 38:-1, 39:-1, 48:-1, 49:-1, 50:-1, 51:-1, 52:-1
}


# Next, we need to make a deck shuffler, which will include a randomization function that grabs a random card from a deck of 52 cards (no jokers obviously).
# Since cards that have been drawn are no longer in the deck of available cards, we'll place them into the category "Excluded_Cards".
# The excluded cards include the cards that are currently in play and the cards that are in the discard pile, waiting to be reshuffled when the deck is exhausted.
# Importing random allows for the random function to be called and the excluded cards has nothing in the brackets since the collection of excluded cards starts with nothing.
import random
Excluded_Cards = []

# Here, we define a function "Generate_Random_Card" which will randomly choose a number from 1 to 52, representing a card, according to the dictionary assigned
def Generate_Random_Card():
	Chosen_Card = random.randint(1,52)

# This is where we ensure that the card is actually remaining in the deck by having the program search for a random card. If this card is the same identity number as one 
# that was already pulled, it will run the function again, and again, and again, as many times as it takes until it finds a uniqure identity number between 1 and 52.
# Once it grabs a unique number, it "deals" that card and continues to select random cards and repeat the process.
	while Chosen_Card in Excluded_Cards:
		Chosen_Card = random.randint(1,52)

	return Chosen_Card


# Now, we ask for a card from the dealer program.
Card_1 = Generate_Random_Card()
# The program (deck dealer) meticulously takes note of which cards it has drawn so it doesn't make the mistake of distributing duplicates
Excluded_Cards.append(Card_1)

# When we receive the card, we'd like to know the identity of the card (as opposed to the identity number), and so the program generously tells us the name of the card it deals
Card_1_Name = Card_Names[Card_1]

# This is the card that was drawn first:
print("Your first card is %s!" % Card_1_Name)

# Now, when you're playing blackjack you can play 1 on 1 with the dealer (hopefully intoxicated if that's what it's come to), or with up to 6 players and 1 dealer.
# Here, we'll illustrate your 3 am online gambling escapades by assuming it's just you and the dealer who wonders where her life went wrong:
# This means we're going to see our two cards, and one of the dealers cards (I forgot to mention earlier that the dealer plays one of their cards up when they deal)
# So, let's draw another two cards to see what they would be. We'll use the same code as before for drawing cards, but now define two new cards: Card_2 & Card_3

Card_2 = Generate_Random_Card()
Excluded_Cards.append(Card_2)
Card_2_Name = Card_Names[Card_2]
print("Your second card is %s!" % Card_2_Name)

Card_3 = Generate_Random_Card()
Excluded_Cards.append(Card_3)
Card_3_Name = Card_Names[Card_3]
print("The dealer's first card is %s!" % Card_3_Name)


# Now we need a function that can keep the current count: Calculate_Count will do the job by taking the input which is the collection of discarded cards (Excluded_Cards)
def Calculate_Count(Excluded_Cards):
# We'll need to define our count variable (Current_Count) as a value which will get replaced when we call the function later.
	Current_Count = 0
# This for loop will take the count of each of the cards in the excluded cards collection and sum the values, effectively returning the total count
	for card in Excluded_Cards:
		Current_Count += Card_Counts[card]
	return Current_Count

# Here we call the function Calculate_Count which takes our input values (the identity number from the first library), and converts it to the count value (defined in the second library)
# for each of the cards in the discard pile.
Current_Count = Calculate_Count(Excluded_Cards)
print("The current count before the 'hit phase' is %s." % Current_Count)


# Part 2
"""
The dealer strategy (as defined before) follows these rules:
1. If the sum of the points the dealer has is < or = 16, the dealer must take a hit.
2. If the sum of the points the dealer has is > 16, the dealer must not take a hit (must stay).

The player strategy is more complicated as it depends on the count.
Lets keep it fairly simple, by staying to the following rules:
1. If the sum of points is <12, you must take a hit since there is no risk involved, and almost never anything to be gained from staying at a very low number.
2. If the sum of points is =17, you're going to stay unless the count is -3 or less.
3. If the sum of points is =16, you're going to stay unless the count is -2 or less.
4. If the sum of points is =15, you're going to stay unless the count is -1 or less.
5. If the sum of points is =14, you're going to stay unless the count is 0 or less.
6. If the sum of points is =13, you're going to stay unless the count is +1 or less.
7. If the sum of points is =12, you're going to stay unless the count is +2 or less.
"""

# Let's introduce your hand as a sum of points. For this, we'll make library 3, which assigns the card identity to its point value.

Card_Points = {
1: 2,
2: 3,
3: 4,
4: 5,
5: 6,
6: 7,
7: 8,
8: 9,
9: 10,
10: 10,
11: 10,
12: 10,
13: 11,
14: 2,
15: 3,
16: 4,
17: 5,
18: 6,
19: 7,
20: 8,
21: 9,
22: 10,
23: 10,
24: 10,
25: 10,
26: 11,
27: 2,
28: 3,
29: 4,
30: 5,
31: 6,
32: 7,
33: 8,
34: 9,
35: 10,
36: 10,
37: 10,
38: 10,
39: 11,
40: 2,
41: 3,
42: 4,
43: 5,
44: 6,
45: 7,
46: 8,
47: 9,
48: 10,
49: 10,
50: 10,
51: 10,
52: 11,
}

# At this point we'll introduce both of the hands, stating what cards we start with, the value of those cards, and the total count
Cards_In_Hand = []
Cards_In_Hand.append(Card_1)
Cards_In_Hand.append(Card_2)
Hand_Points = Card_Points[Card_1] + Card_Points[Card_2]

Cards_In_Dealers_Hand = []
Cards_In_Hand.append(Card_3)
Dealers_Hand_Points = Card_Points[Card_3]

print("The value of your starting hand is %s: " % Hand_Points)

# Now we exercise our moves according to the ruleset defined for the player
while Hand_Points <= 17:

	if Hand_Points < 12 or (Hand_Points == 12 and Current_Count <= 2) or (Hand_Points == 13 and Current_Count <= 1) or (Hand_Points == 14 and Current_Count <= 0)  or (Hand_Points == 15 and Current_Count <= -1) or (Hand_Points == 16 and Current_Count <= -2) or (Hand_Points == 17 and Current_Count <= -3):
		Hit_Card = Generate_Random_Card()
		Excluded_Cards.append(Hit_Card)
		Cards_In_Hand.append(Hit_Card)
		Hit_Card_Name = Card_Names[Hit_Card]
		Hand_Points += Card_Points[Hit_Card]
		print("You hit, and your next card is %s!" % Hit_Card_Name)
		print("Now, the value of your hand is %s: " % Hand_Points)

	else: 
		print("The value of your final hand is %s:" % Hand_Points)
		break
Current_Count = Calculate_Count(Excluded_Cards)
if Hand_Points > 21:
	print("You bust!")
else:
	print("The count after your turn is: %s" % Current_Count)
	while Dealers_Hand_Points < 17:
		Dealers_Hit_Card = Generate_Random_Card()
		Excluded_Cards.append(Dealers_Hit_Card)	
		Cards_In_Dealers_Hand.append(Dealers_Hit_Card)
		Dealers_Hit_Card_Name = Card_Names[Dealers_Hit_Card]
		Dealers_Hand_Points += Card_Points[Dealers_Hit_Card]
		print("The dealer takes a hit and her next card is %s!" % Dealers_Hit_Card_Name)
		print("Now, the value of the dealer's hand is %s!" % Dealers_Hand_Points)
		break
Current_Count = Calculate_Count(Excluded_Cards)
print("The count after the round is %s!" %Current_Count)

if Hand_Points <= 21 and Hand_Points > Dealers_Hand_Points:
	print("You won!")