# Introductory stuff

import math


# Box (rectangular prism)

def areaOfBox():
	length = float(input("Enter a length: "))
	width = float(input("Enter a width: "))
	height = float(input("Enter a height: "))
	area = 2 * length * width + 2 * length * height + 2 * width * height

	if length < 0 or width < 0 or height < 0:
		print("These need to be positive values!")
	else:
		print("The area is {:.2f}!".format(area))


def volumeOfBox():
	length = float(input("Enter a length: "))
	width = float(input("Enter a width: "))
	height = float(input("Enter a height: "))
	volume = length * width * height

	if length < 0 or width < 0 or height < 0:
		print("These need to be positive values!")
	else:
		print("The volume is {:.2f}!".format(volume))

# Sphere 

def areaOfSphere():
	radius = float(input("Enter the radius: "))
	area = 4 * math.pi * radius ** 2

	if radius < 0:
		print("The radius must be a positive value!")
	else:
		print("The area is {:.2f}!".format(area))


def volumeOfSphere():
	radius = float(input("Enter the radius: "))
	volume = (4/3) * math.pi * radius ** 3

	if radius < 0:
		print("The radius must be a positive value!")
	else:
		print("The volume is {:.2f}!".format(volume))


# Calling the necessary function:

def callMeBaby():
	areaOrVolume = input("Type 'area' or 'volume':")

	if areaOrVolume == 'area':
		print("Cool, you chose area\nThis calculator can help with the following:\nBox, Sphere")

		shape = input("Type 'box' or 'sphere': ")

		if shape == 'box':
			areaOfBox()
		elif shape == 'sphere':
			areaOfSphere()
		else:
			print("Hey buckaroo, you need to type either 'box' or 'sphere'... back to the lobby!")

	elif areaOrVolume == 'volume':
		print("Sweet, you chose volume\nThis calculator can help with the following:\nBox, Sphere") 

		shape = input("Type 'box' or 'sphere': ")

		if shape == 'box':
			volumeOfBox()
		elif shape == 'sphere':
			areaOfSphere()
		else:
			print("Hey buckaroo, you need to type either 'box' or 'sphere'... back to the lobby!")

	else:
		print("Hey buckaroo, you need to type either 'area' or 'volume'... back to the lobby!")

callMeBaby()