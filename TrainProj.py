import random

def vertOrHorLight():
	global currentLight
	upOrDown = random.randint(1,2)
	if upOrDown == 1:
		currentLight = "vertical"
	elif upOrDown == 2:
		currentLight = "horizontal"
	print(f"The current light is {currentLight}")

def timeLeft():
	global time
	time = random.randint(3,35)
	print(f"Before crossing, there are {time} seconds left on the clock")

def ableToCross():
	global canCross
	if time < 6:
		canCross = False
		print("You need to wait for the light to switch")
	else:
		canCross = True
		print("There's enough time to cross the block")

def move():
	global duration
	global rightPos
	global upPos
	if currentLight == "vertical" and canCross == True:
		upPos += 1
		duration += 6
	elif currentLight == "horizontal" and canCross == True:
		rightPos += 1
		duration += 6
	elif canCross == False:
		if currentLight == "vertical" and rightPos < horizontalBlocks:
			rightPos += 1
			duration += time + 6
		elif currentLight == "horizontal" and upPos < vericalBlocks:
			upPos += 1
			duration += time + 6
		elif currentLight == "vertical" and rightPos == horizontalBlocks and upPos < vericalBlocks:
			upPos += 1
			duration += time + 6 + 35
		elif currentLight == "horizontal" and upPos == vericalBlocks and rightPos < horizontalBlocks:
			rightPos += 1
			duration += time + 6 + 35
	print(f"The current position is: ({rightPos},{upPos}), and the current duration is {duration}")

rightPos = 0
upPos = 0
duration = 0
vericalBlocks = random.randint(3,10)
horizontalBlocks = random.randint(3,10)

print(f"The number of vertical blocks is {vericalBlocks}, and the number of horizontal blocks is {horizontalBlocks}!")

vertOrHorLight()
timeLeft()
ableToCross()
move()