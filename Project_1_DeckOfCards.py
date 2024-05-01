# This program will assign a number value to each card
# Then the program will randomly draw a card and remove the card from the "deck"

# There are four "suits" of cards, and 13 "identities" for each suit, totaling 52 cards (note jokers are excluded from this deck)
# Starting by hardcoding a number value for each specific card so the program can have an identity for each card


# This part of the program will randomly declare a number between 1 and 52, effectively choosing a random card from the deck of cards and print the card that was chosen

import random
Excluded_Cards = []
def generate_random_card():
	Chosen_Card = random.randint(1,52)
	while Chosen_Card in Excluded_Cards:
		Chosen_Card = random.randint(1,52)
	return Chosen_Card

# Writing a dictionary to map card names
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
52: "ace of clubs",
}
# Selecting card and giving it a name
Card_1 = generate_random_card()
Excluded_Cards.append(Card_1)
Card_2 = generate_random_card()
Excluded_Cards.append(Card_2)
Card_3 = generate_random_card()
Excluded_Cards.append(Card_3)
Card_4 = generate_random_card()
Excluded_Cards.append(Card_4)
Card_5 = generate_random_card()
Excluded_Cards.append(Card_5)
Card_6 = generate_random_card()
Excluded_Cards.append(Card_6)
Card_7 = generate_random_card()
Excluded_Cards.append(Card_7)
Card_8 = generate_random_card()
Excluded_Cards.append(Card_8)
Card_9 = generate_random_card()
Excluded_Cards.append(Card_9)
Card_10 = generate_random_card()
Excluded_Cards.append(Card_10)
Card_11 = generate_random_card()
Excluded_Cards.append(Card_11)
Card_12 = generate_random_card()
Excluded_Cards.append(Card_12)
Card_13 = generate_random_card()
Excluded_Cards.append(Card_13)
Card_14 = generate_random_card()
Excluded_Cards.append(Card_14)
Card_15 = generate_random_card()
Excluded_Cards.append(Card_15)
Card_16 = generate_random_card()
Excluded_Cards.append(Card_16)
Card_17 = generate_random_card()
Excluded_Cards.append(Card_17)
Card_18 = generate_random_card()
Excluded_Cards.append(Card_18)
Card_19 = generate_random_card()
Excluded_Cards.append(Card_19)
Card_20 = generate_random_card()
Excluded_Cards.append(Card_20)
Card_21 = generate_random_card()
Excluded_Cards.append(Card_21)
Card_22 = generate_random_card()
Excluded_Cards.append(Card_22)
Card_23 = generate_random_card()
Excluded_Cards.append(Card_23)
Card_24 = generate_random_card()
Excluded_Cards.append(Card_24)
Card_25 = generate_random_card()
Excluded_Cards.append(Card_25)
Card_26 = generate_random_card()
Excluded_Cards.append(Card_26)
Card_27 = generate_random_card()
Excluded_Cards.append(Card_27)
Card_28 = generate_random_card()
Excluded_Cards.append(Card_28)
Card_29 = generate_random_card()
Excluded_Cards.append(Card_29)
Card_30 = generate_random_card()
Excluded_Cards.append(Card_30)
Card_31 = generate_random_card()
Excluded_Cards.append(Card_31)
Card_32 = generate_random_card()
Excluded_Cards.append(Card_32)
Card_33 = generate_random_card()
Excluded_Cards.append(Card_33)
Card_34 = generate_random_card()
Excluded_Cards.append(Card_34)
Card_35 = generate_random_card()
Excluded_Cards.append(Card_35)
Card_36 = generate_random_card()
Excluded_Cards.append(Card_36)
Card_37 = generate_random_card()
Excluded_Cards.append(Card_37)
Card_38 = generate_random_card()
Excluded_Cards.append(Card_38)
Card_39 = generate_random_card()
Excluded_Cards.append(Card_39)
Card_40 = generate_random_card()
Excluded_Cards.append(Card_40)
Card_41 = generate_random_card()
Excluded_Cards.append(Card_41)
Card_42 = generate_random_card()
Excluded_Cards.append(Card_42)
Card_43 = generate_random_card()
Excluded_Cards.append(Card_43)
Card_44 = generate_random_card()
Excluded_Cards.append(Card_44)
Card_45 = generate_random_card()
Excluded_Cards.append(Card_45)
Card_46 = generate_random_card()
Excluded_Cards.append(Card_46)
Card_47 = generate_random_card()
Excluded_Cards.append(Card_47)
Card_48 = generate_random_card()
Excluded_Cards.append(Card_48)
Card_49 = generate_random_card()
Excluded_Cards.append(Card_49)
Card_50 = generate_random_card()
Excluded_Cards.append(Card_50)
Card_51 = generate_random_card()
Excluded_Cards.append(Card_51)
Card_52 = generate_random_card()

# Naming the cards
Card_1_Name = Card_Names[Card_1]
Card_2_Name = Card_Names[Card_2]
Card_3_Name = Card_Names[Card_3]
Card_4_Name = Card_Names[Card_4]
Card_5_Name = Card_Names[Card_5]
Card_6_Name = Card_Names[Card_6]
Card_7_Name = Card_Names[Card_7]
Card_8_Name = Card_Names[Card_8]
Card_9_Name = Card_Names[Card_9]
Card_10_Name = Card_Names[Card_10]
Card_11_Name = Card_Names[Card_11]
Card_12_Name = Card_Names[Card_12]
Card_13_Name = Card_Names[Card_13]
Card_14_Name = Card_Names[Card_14]
Card_15_Name = Card_Names[Card_15]
Card_16_Name = Card_Names[Card_16]
Card_17_Name = Card_Names[Card_17]
Card_18_Name = Card_Names[Card_18]
Card_19_Name = Card_Names[Card_19]
Card_20_Name = Card_Names[Card_20]
Card_21_Name = Card_Names[Card_21]
Card_22_Name = Card_Names[Card_22]
Card_23_Name = Card_Names[Card_23]
Card_24_Name = Card_Names[Card_24]
Card_25_Name = Card_Names[Card_25]
Card_26_Name = Card_Names[Card_26]
Card_27_Name = Card_Names[Card_27]
Card_28_Name = Card_Names[Card_28]
Card_29_Name = Card_Names[Card_29]
Card_30_Name = Card_Names[Card_30]
Card_31_Name = Card_Names[Card_31]
Card_32_Name = Card_Names[Card_32]
Card_33_Name = Card_Names[Card_33]
Card_34_Name = Card_Names[Card_34]
Card_35_Name = Card_Names[Card_35]
Card_36_Name = Card_Names[Card_36]
Card_37_Name = Card_Names[Card_37]
Card_38_Name = Card_Names[Card_38]
Card_39_Name = Card_Names[Card_39]
Card_40_Name = Card_Names[Card_40]
Card_41_Name = Card_Names[Card_41]
Card_42_Name = Card_Names[Card_42]
Card_43_Name = Card_Names[Card_43]
Card_44_Name = Card_Names[Card_44]
Card_45_Name = Card_Names[Card_45]
Card_46_Name = Card_Names[Card_46]
Card_47_Name = Card_Names[Card_47]
Card_48_Name = Card_Names[Card_48]
Card_49_Name = Card_Names[Card_49]
Card_50_Name = Card_Names[Card_50]
Card_51_Name = Card_Names[Card_51]
Card_52_Name = Card_Names[Card_52]

# Displaying the cards drawn in their respective order

# Here we ask the user if he or she would like to see the exhaustive list of cards drawn in their respective order:
x = input("Would you like to see the exhaustive list in which the cards were drawn? Enter 'yes' if you would, otherwise type anything else if you would not like to")
if x == "yes":
	print("The first randomly chosen card is the %s!" % Card_1_Name)
	print("The second randomly chosen card is the %s!" % Card_2_Name)
	print("The third randomly chosen card is the %s!" % Card_3_Name)
	print("The fourth randomly chosen card is the %s!" % ard_4_Name)
	print("The fifth randomly chosen card is the %s!" % Card_5_Name)
	print("The sixth randomly chosen card is the %s!" % Card_6_Name)
	print("The seventh randomly chosen card is the %s!" % Card_7_Name)
	print("The eighth randomly chosen card is the %s!" % Card_8_Name)
	print("The ninth randomly chosen card is the %s!" % Card_9_Name)
	print("The tenth randomly chosen card is the %s!" % Card_10_Name)
	print("The eleventh randomly chosen card is the %s!" % Card_11_Name)
	print("The twelfth randomly chosen card is the %s!" % Card_12_Name)
	print("The thirteenth randomly chosen card is the %s!" % Card_13_Name)
	print("The fourteenth randomly chosen card is the %s!" % Card_14_Name)
	print("The fifteenth randomly chosen card is the %s!" % Card_15_Name)
	print("The sixteenth randomly chosen card is the %s!" % Card_16_Name)
	print("The seventeenth randomly chosen card is the %s!" % Card_17_Name)
	print("The eighteenth randomly chosen card is the %s!" % Card_18_Name)
	print("The ninteenth randomly chosen card is the %s!" % Card_19_Name)
	print("The twentieth randomly chosen card is the %s!" % Card_20_Name)
	print("The twenty first randomly chosen card is the %s!" % Card_21_Name)
	print("The twenty second randomly chosen card is the %s!" % Card_22_Name)
	print("The twenty third randomly chosen card is the %s!" % Card_23_Name)
	print("The twenty fourth randomly chosen card is the %s!" % Card_24_Name)
	print("The twenty fifty randomly chosen card is the %s!" % Card_25_Name)
	print("The twenty sixth randomly chosen card is the %s!" % Card_26_Name)
	print("The twenty seventh randomly chosen card is the %s!" % Card_27_Name)
	print("The twenty eighth randomly chosen card is the %s!" % Card_28_Name)
	print("The twenty ninth randomly chosen card is the %s!" % Card_29_Name)
	print("The thirtieth randomly chosen card is the %s!" % Card_30_Name)
	print("The thirty first randomly chosen card is the %s!" % Card_31_Name)
	print("The thirty second randomly chosen card is the %s!" % Card_32_Name)
	print("The thirty third randomly chosen card is the %s!" % Card_33_Name)
	print("The thirty fourth randomly chosen card is the %s!" % Card_34_Name)
	print("The thirty fifth randomly chosen card is the %s!" % Card_35_Name)
	print("The thirty sixth randomly chosen card is the %s!" % Card_36_Name)
	print("The thirty seventh randomly chosen card is the %s!" % Card_37_Name)
	print("The thirty eighth randomly chosen card is the %s!" % Card_38_Name)
	print("The thirty ninth randomly chosen card is the %s!" % Card_39_Name)
	print("The fortieth randomly chosen card is the %s!" % Card_40_Name)
	print("The forty first randomly chosen card is the %s!" % Card_41_Name)
	print("The forty second randomly chosen card is the %s!" % Card_42_Name)
	print("The forty third randomly chosen card is the %s!" % Card_43_Name)
	print("The forty fourth randomly chosen card is the %s!" % Card_44_Name)
	print("The forty fifth randomly chosen card is the %s!" % Card_45_Name)
	print("The forty sixth randomly chosen card is the %s!" % Card_46_Name)
	print("The forty seventh randomly chosen card is the %s!" % Card_47_Name)
	print("The forty eighth randomly chosen card is the %s!" % Card_48_Name)
	print("The forty ninth randomly chosen card is the %s!" % Card_49_Name)
	print("The fiftieth randomly chosen card is the %s!" % Card_50_Name)
	print("The fifty first randomly chosen card is the %s!" % Card_51_Name)
	print("The fifty second randomly chosen card is the %s!" % Card_52_Name)
elif x!= "yes":
	print("Very well.")