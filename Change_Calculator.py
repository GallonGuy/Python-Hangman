import random
import math
import matplotlib.pyplot as plt

# This Part describes the cost of the items in the shopping cart, and how much money you spend on them (assuming you only carry $50 dollar bills like a baller)
Item_Cost = round(random.uniform(1,200), 2)
print("Your items costs $%s" %Item_Cost)
Money_Paid = math.ceil(Item_Cost/50)*50
print("You pay $%s for the items." %Money_Paid)
Money_Due = round(Money_Paid - Item_Cost, 2)
print("The money the you should receive back is $%s" %Money_Due)

# Next, we'll introduce several variables representing increments of money that may come back to you
Num_20s_Due = 0
Num_10s_Due = 0
Num_5s_Due = 0
Num_1s_Due = 0
Quarters_Due = 0
Dimes_Due = 0
Nickels_Due = 0
Pennies_Due = 0

# We'll also introduce several variables that represent the amount of each increment and the decimal
Decimal_20s = 0
Decimal_10s = 0
Decimal_5s = 0
Decimal_1s = 0
Decimal_Quarters = 0
Decimal_Dimes = 0
Decimal_Nickels = 0

# Next, we'll use the floor function to determine how many of each currency should be returned
Num_20s_Due = math.floor(Money_Due/20)
Money_Due -= 20 * Num_20s_Due
Num_10s_Due = math.floor(Money_Due/10)
Money_Due -= 10 * Num_10s_Due
Num_5s_Due = math.floor(Money_Due/5)
Money_Due -= 5 * Num_5s_Due
Num_1s_Due = math.floor(Money_Due/1)
Money_Due -= 1 * Num_1s_Due
Quarters_Due = math.floor(Money_Due/0.25)
Money_Due -= 0.25 * Quarters_Due
Dimes_Due = math.floor(Money_Due/0.1)
Money_Due -= 0.1 * Dimes_Due
Nickels_Due = math.floor(Money_Due/0.05)
Money_Due -= 0.05 * Nickels_Due
Pennies_Due = math.floor(Money_Due/0.01)
Money_Due -= 0.01 * Pennies_Due
print("We receive: %s 20's, %s 10's, %s 5's, %s 1's, %s quarters, %s dimes, %s nickels, and %s pennies" %(Num_20s_Due,Num_10s_Due,Num_5s_Due,Num_1s_Due,Quarters_Due,Dimes_Due,Nickels_Due,Pennies_Due))

# Create lists of currency types and their corresponding amounts
currency_types = ['Twenties', 'Tens', 'Fives', 'Singles', 'Quarters', 'Dimes', 'Nickels', 'Pennies']
currency_amounts = [Num_20s_Due, Num_10s_Due, Num_5s_Due, Num_1s_Due, Quarters_Due, Dimes_Due, Nickels_Due, Pennies_Due]

# Demonstrating each currency in a bar graph
plt.bar(currency_types, currency_amounts)
plt.xlabel('Currency Types')
plt.ylabel('Amounts')
plt.title('Currency Distribution')
plt.yticks(range(int(max(currency_amounts)) + 1))
plt.show()