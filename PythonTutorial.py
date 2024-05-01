
x = 0
i = 0

while i < 10:
	i += 1
	x = i
	if i == 3:
		x_3rd = x
	if i ==9:
		x_9th = x

print("The third value of x is equal to", x_3rd)
print("The ninth value of x is equal to",x_9th)

a = 6
b = 5
for i in range(1,100):
    a += 1
    if a % b ==0:
        break

print("The first value that is divisible by", b ,"in this sequence is:",a)

import random

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random number between 1 and 1000
n = random.randint(1, 1000)

# Check if random number is prime and print result
if is_prime(n):
    print(n, "is prime")
else:
    print(n, "is not prime")

import random

# This code will test if the number is even
# If the value is even it will double it
# If the value is odd, it will multiply it by 3 and add 1 to the value

r = random.randint(1,3000)
i = 0
r_values = [r]
while r != 1:
    if r % 2 == 0:
        r = r / 2
    else:
     r = 3 * r + 1
    i += 1

print("the number of iterations is",i)

money_in_wallet = 40
sandwich_price = 7.50
sales_tax = 0.08 * sandwich_price
sandwich_price += sales_tax
money_in_wallet -= sandwich_price

print("The new sandwich price is "+str(sandwich_price))
print("The remaining money in the wallet is "+str(money_in_wallet))

# We can also use the subsitution method to write this code
# This is advantageous because we can make the sentences appear more normal when reading with less overall effort ($ and . in this case):

print("The new sandwich price is $%s." %sandwich_price)
print("The remaining money in the wallet is $%s." %money_in_wallet)
