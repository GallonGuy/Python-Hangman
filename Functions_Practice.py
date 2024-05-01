# Functions practice

import random
import matplotlib


def func1():
    print("The is the most basic function.")
    print("hello")

func1() # Call the function

def countingInPrimes():
    rangeBottom = random.randint(90, 100)
    print("The bottom number is %s." % rangeBottom)
    rangeTop = random.randint(120, 130)
    print("The top number is %s." % rangeTop)
    tempVariable = rangeBottom
    primeList = []

    while tempVariable < rangeTop:
        valid = True

        for value in range(2, int(tempVariable ** 0.5) + 1):
            if tempVariable % value == 0:
                valid = False
                break

        if valid:
            primeList.append(tempVariable)

        tempVariable += 1
    print("The primes are: %s" % primeList)

countingInPrimes()

def computepay(h,r):

    if h <= 40:
        totalPay = h * r
        return totalPay
    elif 40 < h:
        grossPay = 40 * r
        overtimePay = 1.5 * r * (h - 40)
        totalPay = grossPay + overtimePay
        return totalPay
    else: 
        print("You need to have a positive number of hours")

#  = computepay(float(input("How many hours")),float(input("Hourly wage")))
# print("Pay",p)

def breakCon():

    letters = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z",
    }

    randomLetter = letters[random.randint(1,26)]
    print("The random letter is:",randomLetter)

    for letter in letters.values():
        print(letter)
        if letter == randomLetter:
            break
    print("\nDone with the break but now it's time for continue:\n")

    for letter in letters.values():
        if letter == randomLetter:
            continue
        print(letter)

breakCon()



