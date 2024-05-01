#PY4E
'''

x = input("What name would you like?")
print(f"Hello {x}")

-

hours = float(input("How many hours are you working?"))
rate = float(input("What is your hourly rate?"))
pay = hours * rate
print(f"Pay: {pay}")

-

hours = float(input("How many hours did you work?"))
rate = float(input("What is the hourly rate?"))

if hours > 40:
	overtimeHours = hours - 40
	pay = 40 * rate + overtimeHours * rate * 1.5
else:
	pay = hours * rate
print(pay)

-

score = None
while score == None or score < 0 or score > 1.0:
	score = float(input("What did you get in the class (if you got a 61%, type '61')"))
	score = score / 100

if score >= 0.9:
	print("A")
elif score < 0.9 and score >= 0.8:
	print("B")
elif score < 0.8 and score >= 0.7:
	print("C")
elif score < 0.7 and score >= 0.6:
	print("D")
else:
	print("F")
'''


def computepay():
	global pay

	try:
		hours = float(input("How many hours, pal?"))
		rate = float(input("What's the rate, pal?"))
	except:
		print('You fucked up, pal (Invalid input)')
		return

	if hours < 0 or rate < 0:
		print('You fucked up, pal (Negative number)')
		return

	if hours > 40:
		pay = (hours - 40) * (rate * 1.5) + 40 * rate
	else:
		pay = hours * rate
	print(f"{pay:.2f}")

computepay()

















