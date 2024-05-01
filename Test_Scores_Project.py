# Creating a Deck of cards using the class "Card"
import random

class Card:
    def __init__(self,Rank,Suit,Count_Value,Points):
        self.Rank = Rank
        self.Suit = Suit
        self.Count_Value = Count_Value
        self.Points = Points

    def Get_Suit(self):
        return self.Suit

    def Get_Rank(self):
        return self.Rank

    def Get_Count_Value(self):
        return self.Count_Value

    def Get_Points(self):
        return self.Points

def Create_Deck():
    Ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    Suits = ["Diamonds","Hearts","Clubs","Spades"]
    Low_Cards = ["2", "3", "4", "5", "6"]
    Mid_Cards = ["7","8","9"]
    High_Cards = ["10", "Jack", "Queen", "Ace"]

    Deck = []

    for Suit in Suits:
        for Rank in Ranks:

            if Rank in Low_Cards:
                Count_Value = 1
                Points = int(Rank)
            elif Rank in Mid_Cards:
                Count_Value = 0
                Points = int(Rank)
            elif Rank in High_Cards:
                Count_Value = -1
                Points = 10
                if Rank == "Ace":
                    Points = 11

            New_Card = Card(Rank, Suit, Count_Value, Points)
            Deck.append(New_Card)

    return Deck

Deck_Of_Cards = Create_Deck()


def Assign_Turns():
    Turn = []
    y = 1
    Current_Turn = 1
    Number_Of_Players = random.randint(1,7)
    Player_Turn = random.randint(1,Number_Of_Players)
    print("The number of AI players is %s." %Number_Of_Players)
    print("There will be %s players who will draw cards before you." %(Player_Turn-1))

    while y < Player_Turn:
        Turn.append(y)
        y += 1

    while y == Player_Turn:
        Turn.append(69)
        y += 1

    while y > Player_Turn and y < (Number_Of_Players + 2):
        Turn.append(y - 1)
        y += 1

    while y == Number_Of_Players + 2:
        Turn.append(420)
        y += 1

    return Turn, Number_Of_Players, Player_Turn, Current_Turn


def Draw_A_Card():
    if len(Deck_Of_Cards) > 1:
        Random_Index = random.randint(0,len(Deck_Of_Cards)-1)
        # print("The number of cards remaining in the deck is:",len(Deck_Of_Cards))
        Random_Card = Deck_Of_Cards[Random_Index]
        # print("The card that was pulled was the", Random_Card.Get_Rank(),"of", Random_Card.Get_Suit())
        # Discard_Pile.append(Random_Card)
        Deck_Of_Cards.remove(Random_Card)
        return Random_Card
    elif len(Deck_Of_Cards) == 1:
        Final_Card = Deck_Of_Cards[0]
        # Discard_Pile.append(Deck_Of_Cards[0])
        Deck_Of_Cards.remove(Deck_Of_Cards[0])
        return Final_Card
    else:
        print("The deck has no cards left to draw from")


# Game Mechanincs

def Play_Game():

# Initializing variables:

    P1_Hand = []
    P2_Hand = []
    P3_Hand = []
    P4_Hand = []
    P5_Hand = []
    P6_Hand = []
    P7_Hand = []
    Discard_Pile = []
    Visible_Discard = []
    Player_Hand = []
    Dealer_Hand = []
    x = 1

    Turn, Number_Of_Players, Player_Turn, Current_Turn = Assign_Turns()
    print("Turn is: %s" %Turn)

    # Number_Of_Players = int(input("How many players are there (Not including dealer & max = 7 players)"))
    # Player_Turn = int(input("What seat are you at the table? (if you're the third player delt cards, type 3)"))
    # Distributing turns according to where the player is sitting

    # Starting turn where everyone gets delt cards

    Player_Hand.append(Draw_A_Card())
    Visible_Discard.append(Player_Hand[-1])
    print("Hand Card 1:",Player_Hand[-1].Get_Rank())
    Player_Hand.append(Draw_A_Card())
    Visible_Discard.append(Player_Hand[-1])
    print("Hand Card 2:",Player_Hand[-1].Get_Rank())
    Dealer_Hand.append(Draw_A_Card())
    Visible_Discard.append(Dealer_Hand[-1])
    print("Dealer's visible card is:",Dealer_Hand[-1].Get_Rank())
    Dealer_Hand.append(Draw_A_Card())
    print("Before the cards are delt, the current count is %s." %sum(Card.Get_Count_Value() for Card in Visible_Discard))

    P1_Hand.extend([Draw_A_Card() for _ in range(2)])
    if Number_Of_Players > 1: 
        P2_Hand.extend([Draw_A_Card() for _ in range(2)])
    if Number_Of_Players > 2:
        P3_Hand.extend([Draw_A_Card() for _ in range(2)])
    if Number_Of_Players > 3:
        P4_Hand.extend([Draw_A_Card() for _ in range(2)])
    if Number_Of_Players > 4:
        P5_Hand.extend([Draw_A_Card() for _ in range(2)])
    if Number_Of_Players > 5:
        P6_Hand.extend([Draw_A_Card() for _ in range(2)])
    if Number_Of_Players > 6:
        P7_Hand.extend([Draw_A_Card() for _ in range(2)])

    while len(Turn) > 0:

        while Turn[0] == 69:
            # print("At the start of your turn, the count is:", sum(Card.Get_Count_Value() for Card in Visible_Discard))
            # print("Remember the sum of points in your hand is %s." %sum(Card.Get_Points() for Card in Player_Hand))

            if sum(Card.Get_Points() for Card in Player_Hand) >21 or x != 1:
                print("You bust!")
                print("The turn has been passed.")
                Turn.pop(0)

            elif Turn[0] == 69 and x == 1 and sum(Card.Get_Points() for Card in Player_Hand) <= 21: # This or turns to an "and" so that the loop works correctly
                Player_Hand.append(Draw_A_Card())
                Visible_Discard.append(Player_Hand[-1])
                print("You drew the %s of %s." % (Player_Hand[-1].Get_Rank(),Player_Hand[-1].Get_Suit()))
                # if int(input("Type 1 for another card, otherwise press any other number")) != 1:
                # Turn.pop(0) # remember to tab this over
                print("Your hand totals %s and the current count is %s." % (sum(Card.Get_Points() for Card in Player_Hand),sum(Card.Get_Count_Value() for Card in Visible_Discard)))
            # print("The visible cards in the discard pile:",([Card.Get_Points() for Card in Visible_Discard])) 


        while len(Turn) > 0 and Turn[0] == 1:
            print("The current turn is: %s." % Turn[0])

            while sum(Card.Get_Points() for Card in P1_Hand) < 17:
                P1_Hand.append(Draw_A_Card())
                print("Player 1 drew the %s of %s." % (P1_Hand[-1].Get_Rank(),P1_Hand[-1].Get_Suit()))
                Visible_Discard.append(P1_Hand[-1])
                print("The current count is now:", sum((Card.Get_Count_Value()) for Card in Visible_Discard))

            if 17 <= sum(Card.Get_Points() for Card in P1_Hand) <= 21:
               Turn.pop(0)

            if sum(Card.Get_Points() for Card in P1_Hand) > 21:
                print("Player 1 has busted!")
                Visible_Discard.append(P1_Hand[0])
                Visible_Discard.append(P1_Hand[1])
                # print([Card.Get_Points() for Card in Visible_Discard])
                print("The current count is: %s." % sum((Card.Get_Count_Value()) for Card in Visible_Discard))
                Turn.pop(0)


        while len(Turn) > 0 and Turn[0] == 2:
            print("The current turn is: %s." % Turn[0])

            while sum(Card.Get_Points() for Card in P2_Hand) < 17:
                P2_Hand.append(Draw_A_Card())
                print("Player 2 drew the %s of %s." % (P2_Hand[-1].Get_Rank(),P2_Hand[-1].Get_Suit()))
                Visible_Discard.append(P2_Hand[-1])
                print("The current count is now:", sum((Card.Get_Count_Value()) for Card in Visible_Discard))

            if 17 <= sum(Card.Get_Points() for Card in P2_Hand) <= 21:
               Turn.pop(0)

            if sum(Card.Get_Points() for Card in P2_Hand) > 21:
                print("Player 2 has busted!")
                Visible_Discard.append(P2_Hand[0])
                Visible_Discard.append(P2_Hand[1])
                # print([Card.Get_Points() for Card in Visible_Discard])
                print("The current count is: %s." % sum((Card.Get_Count_Value()) for Card in Visible_Discard))
                Turn.pop(0)


        while len(Turn) > 0 and Turn[0] == 3:
            print("The current turn is: %s." % Turn[0])

            while sum(Card.Get_Points() for Card in P3_Hand) < 17:
                P3_Hand.append(Draw_A_Card())
                print("Player 3 drew the %s of %s." % (P3_Hand[-1].Get_Rank(),P3_Hand[-1].Get_Suit()))
                Visible_Discard.append(P3_Hand[-1])
                print("The current count is now:", sum((Card.Get_Count_Value()) for Card in Visible_Discard))

            if 17 <= sum(Card.Get_Points() for Card in P3_Hand) <= 21:
               Turn.pop(0)

            if sum(Card.Get_Points() for Card in P3_Hand) > 21:
                print("Player 3 has busted!")
                Visible_Discard.append(P3_Hand[0])
                Visible_Discard.append(P3_Hand[1])
                # print([Card.Get_Points() for Card in Visible_Discard])
                print("The current count is: %s." % sum((Card.Get_Count_Value()) for Card in Visible_Discard))
                Turn.pop(0)


        while len(Turn) > 0 and Turn[0] == 4:
            print("The current turn is: %s." % Turn[0])

            while sum(Card.Get_Points() for Card in P4_Hand) < 17:
                P4_Hand.append(Draw_A_Card())
                print("Player 4 drew the %s of %s." % (P4_Hand[-1].Get_Rank(),P4_Hand[-1].Get_Suit()))
                Visible_Discard.append(P4_Hand[-1])
                print("The current count is now:", sum((Card.Get_Count_Value()) for Card in Visible_Discard))

            if 17 <= sum(Card.Get_Points() for Card in P4_Hand) <= 21:
               Turn.pop(0)

            if sum(Card.Get_Points() for Card in P4_Hand) > 21:
                print("Player 4 has busted!")
                Visible_Discard.append(P4_Hand[0])
                Visible_Discard.append(P4_Hand[1])
                # print([Card.Get_Points() for Card in Visible_Discard])
                print("The current count is: %s." % sum((Card.Get_Count_Value()) for Card in Visible_Discard))
                Turn.pop(0)


        while len(Turn) > 0 and Turn[0] == 5:
            print("The current turn is: %s." % Turn[0])

            while sum(Card.Get_Points() for Card in P5_Hand) < 17:
                P5_Hand.append(Draw_A_Card())
                print("Player 5 drew the %s of %s." % (P5_Hand[-1].Get_Rank(),P5_Hand[-1].Get_Suit()))
                Visible_Discard.append(P5_Hand[-1])
                print("The current count is now:", sum((Card.Get_Count_Value()) for Card in Visible_Discard))

            if 17 <= sum(Card.Get_Points() for Card in P5_Hand) <= 21:
               Turn.pop(0)

            if sum(Card.Get_Points() for Card in P5_Hand) > 21:
                print("Player 5 has busted!")
                Visible_Discard.append(P5_Hand[0])
                Visible_Discard.append(P5_Hand[1])
                # print([Card.Get_Points() for Card in Visible_Discard])
                print("The current count is: %s." % sum((Card.Get_Count_Value()) for Card in Visible_Discard))
                Turn.pop(0)


        while len(Turn) > 0 and Turn[0] == 6:
            print("The current turn is: %s." % Turn[0])

            while sum(Card.Get_Points() for Card in P6_Hand) < 17:
                P6_Hand.append(Draw_A_Card())
                print("Player 6 drew the %s of %s." % (P6_Hand[-1].Get_Rank(),P6_Hand[-1].Get_Suit()))
                Visible_Discard.append(P6_Hand[-1])
                print("The current count is now:", sum((Card.Get_Count_Value()) for Card in Visible_Discard))

            if 17 <= sum(Card.Get_Points() for Card in P6_Hand) <= 21:
               Turn.pop(0)

            if sum(Card.Get_Points() for Card in P6_Hand) > 21:
                print("Player 6 has busted!")
                Visible_Discard.append(P6_Hand[0])
                Visible_Discard.append(P6_Hand[1])
                # print([Card.Get_Points() for Card in Visible_Discard])
                print("The current count is: %s." % sum((Card.Get_Count_Value()) for Card in Visible_Discard))
                Turn.pop(0)


        while len(Turn) > 0 and Turn[0] == 7:
            print("The current turn is: %s." % Turn[0])

            while sum(Card.Get_Points() for Card in P7_Hand) < 17:
                P7_Hand.append(Draw_A_Card())
                print("Player 7 drew the %s of %s." % (P7_Hand[-1].Get_Rank(),P7_Hand[-1].Get_Suit()))
                Visible_Discard.append(P7_Hand[-1])
                print("The current count is now:", sum((Card.Get_Count_Value()) for Card in Visible_Discard))

            if 17 <= sum(Card.Get_Points() for Card in P7_Hand) <= 21:
               Turn.pop(0)

            if sum(Card.Get_Points() for Card in P7_Hand) > 21:
                print("Player 7 has busted!")
                Visible_Discard.append(P7_Hand[0])
                Visible_Discard.append(P7_Hand[1])
                # print([Card.Get_Points() for Card in Visible_Discard])
                print("The current count is: %s." % sum((Card.Get_Count_Value()) for Card in Visible_Discard))
                Turn.pop(0)


        while len(Turn) == 1:
            print("The current turn is: %s." % Turn[0])

            while sum(Card.Get_Points() for Card in Dealer_Hand) < 17:
                Dealer_Hand.append(Draw_A_Card())
                print("The dealer drew the %s of %s." % (Dealer_Hand[-1].Get_Rank(),Dealer_Hand[-1].Get_Suit()))          
                Visible_Discard.append(Dealer_Hand[-1])
                print("The current count is:", sum((Card.Get_Count_Value()) for Card in Visible_Discard))
                print("Dealer's hand sums %s points." %sum(Card.Get_Points() for Card in Dealer_Hand))

            if 17 <= sum(Card.Get_Points() for Card in Dealer_Hand) <= 21:
                Turn.pop(0)

            if sum(Card.Get_Points() for Card in Dealer_Hand) > 21:
                print("Dealer has busted!")
                Visible_Discard.append(Dealer_Hand[1])
                # print([Card.Get_Points() for Card in Visible_Discard])
                Turn.pop(0)

    if sum(Card.Get_Points() for Card in Player_Hand) > sum(Card.Get_Points() for Card in Dealer_Hand) and sum(Card.Get_Points() for Card in Player_Hand) <= 21:
        print("You win!")
    elif sum(Card.Get_Points() for Card in Player_Hand) <= 21 and sum(Card.Get_Points() for Card in Dealer_Hand) > 21:
        print("You win!")
    else:
        print("You lose, Dumbass.")


    # End of round 1

    while len(Visible_Discard) > 0:
        Visible_Discard.remove(Visible_Discard[0])

    print(Visible_Discard)

    for Card in P1_Hand:
        Visible_Discard.append(Card)

    for Card in P2_Hand:
        Visible_Discard.append(Card)

    for Card in P3_Hand:
        Visible_Discard.append(Card)

    for Card in P4_Hand:
        Visible_Discard.append(Card)

    for Card in P5_Hand:
        Visible_Discard.append(Card)

    for Card in P6_Hand:
        Visible_Discard.append(Card)

    for Card in P7_Hand:
        Visible_Discard.append(Card)

    for Card in Player_Hand:
        Visible_Discard.append(Card)

    for Card in Dealer_Hand:
        Visible_Discard.append(Card)

    return Visible_Discard

    print(len(Visible_Discard))
    print("Looking at all of the cards in the discard pile (while definitely not seeming suspicious), the count is: %s" %sum([Card.Get_Count_Value() for Card in Visible_Discard]))

while len(Deck_Of_Cards) > 30:
    Play_Game()
    print(" ")

# TODO:
# Make it an 8 deck shoo
# Make the Game Mechanics run until the deck is out of cards
# Make the ace count for 1 or 11
