# Print 1 through 100
# If num divisible by 3:
	# Print Fizz
# If num divisible by 5:
	# Print Buzz
# If num divisible by 3 & 5:
	# Print FizzBuzz

for i in range(1,101):
	numbers = []
	numbers.append(i)
	if i % 3 == 0 and i % 5 == 0:
		print(i, "FizzBuzz")
	elif i % 3 == 0 and i % 5 != 0:
		print(i, "Fizz")
	elif i % 5 == 0 and i % 3 != 0:
		print(i, "Buzz")
	else:
		print(i)


