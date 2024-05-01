
hrs = input("Enter Hours:")
h = float(hrs)
pay = input("What's the standard hourly wage?")
p = float(pay)

overtimePay = 0
while h > 40:
    overtimePay = 1.5 * (h - 40) * p
    h = h - (h - 40)

standardPay = 0
while h <= 40 and h !=0:
    standardPay = h * p
    h = 0

totalPay = overtimePay + standardPay
print(totalPay)



  
largest = None
smallest = None
myList = []

while True:
    num = input("What integer would you like? Type 'done' to stop inputting values")
    if num == "done":
        break
    try:
        ival = int(num)
        myList.append(ival)
    except:
        print("Invalid input")
    for values in myList:
        if largest is None:
            largest = values
        if smallest is None:
            smallest = values
        if values > largest:
            largest = values
        if values < smallest:
            smallest = values
print("Maximum is",largest)
print("Minimum is",smallest)




line = "Please have a nice day!"
if line.startswith("Please"):
    print("Yep")
if line.startswith("p"):
    print("Yep again!")
else:
    print("You're a goofball, aren't you?")





