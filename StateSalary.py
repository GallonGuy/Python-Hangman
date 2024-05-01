import random
import matplotlib.pyplot as plt
import turtle as t

# Part 1: Importing the Salary Data:

# Federal Tax bracket info link: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets
def checkFederalTaxBracket(income):
	if 0 < income and income < 11000:
		taxRate = 0.1
	elif 11001 < income and income < 44725:
		taxRate = 0.12
	elif 44726 < income and income < 95375:
		taxRate = 0.22
	elif 95376 < income and income < 182100:
		taxRate = 0.24
	elif 182101 < income and income < 231250:
		taxRate = 0.32
	elif 231251 < income and income < 578125:
		taxRate = 0.35
	else:
		taxRate = 578126
	return taxRate

# State Tax Bracket Info Link: https://www.paycom.com/resources/blog/state-income-tax-rates/ 
def checkStateTaxBracket(income, state):

	if state == 'arizona':
		taxRate = 0.025
	elif state == 'colorado':
		taxRate = 0.044
	elif state == 'georgia':
		taxRate = 0.0549
	elif state == 'idaho':
		taxRate = 0.058
	elif state == 'illinois':
		taxRate = 0.0495
	elif state == 'indiana':
		taxRate = 0.0305
	elif state == 'kentucky':
		taxRate = 0.04
	elif state == 'michigan':
		taxRate = 0.0425
	elif state == 'mississippi':
		taxRate = 0.04
	elif state == 'north carolina':
		taxRate = 0.045
	elif state == 'pennsylvania':
		taxRate = 0.0307
	elif state == 'utah':
		taxRate = 0.0465
	elif state == 'alabama':
		if income > 3000:
			taxRate = 0.05
		else:
			taxRate = ((0.05 - 0.02) / (3000 - 0)) * income + 0.02
	elif state == 'arkansas':
		if income > 8000:
			taxRate = 0.044
		else:
			taxRate = ((0.044 - 0.04) / (8000 - 0)) * income + 0.04
	elif state == 'california':
		if income > 1000000:
			taxRate = 0.133
		else:
			taxRate = ((0.133 - 0.01) / (1000000 - 0)) * income + 0.01
	elif state == 'connecticut':
		if income > 500000:
			taxRate = 0.0699
		else:
			taxRate = ((0.0699 - 0.02) / (500000 - 0)) * income + 0.02
	elif state == 'hawaii':
		if income > 200000:
			taxRate = 0.11
		else:
			taxRate = ((0.11 - 0.014) / (200000 - 0)) * income + 0.014
	elif state == 'iowa':
		if income > 62100:
			taxRate = 0.057
		else:
			taxRate = ((0.057 - 0.044) / (62100 - 0)) * income + 0.044
	elif state == 'kansas':
		if income > 30000:
			taxRate = 0.057
		else:
			taxRate = ((0.057 - 0.031) / (30000 - 0)) * income + 0.031
	elif state == 'louisiana':
		if income > 50000:
			taxRate = 0.0425
		else:
			taxRate = ((0.0425 - 0.0185) / (50000 - 0)) * income + 0.0185
	elif state == 'maine':
		if income > 61600:
			taxRate = 0.0715
		else:
			taxRate = ((0.0715 - 0.058) / (61600 - 0)) * income + 0.058
	elif state == 'maryland':
		if income > 250000:
			taxRate = 0.0575
		else:
			taxRate = ((0.0575 - 0.02) / (250000 - 0)) * income + 0.02
	elif state == 'massachusetts':
		if income > 1000000:
			taxRate = 0.09
		else:
			taxRate = ((0.09 - 0.05) / (1000000 - 0)) * income + 0.05
	elif state == 'minnesota':
		if income > 193240:
			taxRate = 0.0985
		else:
			taxRate = ((0.0985 - 0.0535) / (193240 - 0)) * income + 0.0535
	elif state == 'montana':
		if income > 20500:
			taxRate = 0.059
		else:
			taxRate = ((0.059 - 0.047) / (20500 - 0)) * income + 0.047
	elif state == 'nebraska':
		if income > 35730:
			taxRate = 0.0584
		else:
			taxRate = ((0.0584 - 0.0246) / (35730 - 0)) * income + 0.0246
	elif state == 'new jersey':
		if income > 1000000:
			taxRate = 0.1075
		else:
			taxRate = ((0.1075 - 0.014) / (1000000 - 0)) * income + 0.014
	elif state == 'new mexico':
		if income > 210000:
			taxRate = 0.059
		else:
			taxRate = ((0.059 - 0.017) / (210000 - 0)) * income + 0.017
	elif state == 'new york':
		if income > 25000000:
			taxRate = 0.109
		else:
			taxRate = ((0.109 - 0.04) / (25000000 - 0)) * income + 0.04
	elif state == 'oklahoma':
		if income > 7200:
			taxRate = 0.0475
		else:
			taxRate = ((0.0475 - 0.0025) / (7200 - 0)) * income + 0.0025
	elif state == 'oregon':
		if income > 7200:
			taxRate = 0.0475
		else:
			taxRate = ((0.099 - 0.0475) / (7200 - 0)) * income + 0.0475
	elif state == 'rhode island':
		if income > 176050:
			taxRate = 0.0599
		else:
			taxRate = ((0.0599 - 0.0375) / (176050 - 0)) * income + 0.0375
	elif state == 'south carolina':
		if income > 17330:
			taxRate = 0.064
		else:
			taxRate = ((0.064 - 0) / (17330 - 0)) * income + 0
	elif state == 'vermont':
		if income > 229550:
			taxRate = 0.0875
		else:
			taxRate = ((0.0875 - 0.0335) / (229550 - 0)) * income + 0.0335
	elif state == 'virginia':
		if income > 17000:
			taxRate = 0.0575
		else:
			taxRate = ((0.0575 - 0.02) / (17000 - 0)) * income + 0.02
	elif state == 'washington, d.c.':
		if income > 1000000:
			taxRate = 0.1075
		else:
			taxRate = ((0.1075 - 0.04) / (1000000 - 0)) * income + 0.04
	elif state == 'west virginia':
		if income > 60000:
			taxRate = 0.0512
		else:
			taxRate = ((0.0512 - 0.0236) / (60000 - 0)) * income + 0.0236
	elif state == 'wisconsin':
		if income > 315310:
			taxRate = 0.0765
		else:
			taxRate = ((0.0765 - 0.035) / (315310 - 0)) * income + 0.035
	elif state == 'delaware':
		if income < 2000:
			taxRate = 0.022
		elif income > 60000:
			taxRate = 0.066
		else:
			taxRate = ((0.066 - 0.022) / (60000 - 2000)) * income + 0.022
	elif state == 'missouri':
		if income < 1273:
			taxRate = 0.02
		elif income > 8911:
			taxRate = 0.048
		else:
			taxRate = ((0.048 - 0.02) / (8911 - 1273)) * income + 0.02
	elif state == 'north dakota':
		if income < 44725:
			taxRate = 0.0195
		elif income > 225975:
			taxRate = 0.025
		else:
			taxRate = ((0.025 - 0.0195) / (225975 - 44725)) * income + 0.0195
	elif state == 'ohio':
		if income < 26050:
			taxRate = 0.0275
		elif income > 92150:
			taxRate = 0.035
		else:
			taxRate = ((0.035 - 0.0275) / (92150 - 26050)) * income + 0.0275
	elif state == 'alaska' or state == 'florida' or state == 'nevada' or state == 'new hampshire' or state == 'south dakota' or state == 'tennessee' or state == 'texas' or state == 'washington' or state == 'wyoming':
		return 0
	return taxRate

def totalTaxRate(income, state):
	state = state.lower()
	federalTax = checkFederalTaxBracket(income)
	stateTax = checkStateTaxBracket(income, state)
	return federalTax + stateTax

def netIncome(state):
	salary = salaryDict[state]
	taxRate = totalTaxRate(salary, state)
	salary = round(salary * (1 - taxRate), 2)
	return salary

# Average Salary of Software Engineer by State
# Salary Info Link: https://www.ziprecruiter.com/Salaries/What-Is-the-Average-Entry-Level-Software-Engineer-Salary-by-State

def properties(color, location):
     # Moving to starting location
    t.penup()
    t.goto(location)

    # Preparing turtle
    t.fillcolor(color)
    t.pencolor(color)
    t.pendown() # Begins at bottom left and looks right
    t.begin_fill()
    t.left(90) # Rotate to LHS

def textProperties(text):
    
    t.pencolor("black")
    t.write(text, align = "center", font = ("Arial", 12, "normal"))
    t.hideturtle()

def drawWA(location, size, color, text):

    properties(color, location) # Imports starting location and chosen fill color

    # Drawing the state
    t.seth(90)
    t.forward(40)
    t.right(90)
    t.forward(25)
    t.right(45)
    t.forward(5)
    t.left(135)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(35)
    t.left(9)
    t.forward(48)
    t.right(58)
    t.forward(13)
    t.end_fill()
    t.penup()

    text_pos = ((location[0] + size/2) + 10,(location[1] + size/2) - 30)
    t.goto(text_pos)    

    textProperties(text) # Formats and sets location of text

def drawOR(location, size, color, text):

    properties(color, location)

    t.seth(0)
    t.forward(27)
    t.right(55)
    t.forward(14)
    t.left(65)
    t.forward(46)
    t.right(10)
    t.forward(39)
    t.right(45)
    t.forward(11)
    t.right(72)
    t.forward(31)
    t.left(90)
    t.forward(7)
    t.seth(270)
    t.forward(44)
    t.right(90)
    t.forward(119)
    t.end_fill()
    t.penup()

    text_pos = ((location[0] + size/2) + 10,(location[1] + size/2) - 105)
    t.goto(text_pos)    

    textProperties(text)

def drawCA(location, size, color, text):

	properties(color, location)

	t.seth(0)
	t.forward(70)
	t.right(90)
	t.forward(50)
	t.left(45)
	t.forward(130)
	t.right(20)
	t.forward(20)
	t.right(72)
	t.forward(12)
	t.left(47)
	t.forward(25)
	t.right(90)
	t.forward(40)
	t.right(50)
	t.forward(189)
	t.right(40)
	t.forward(49)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 30,(location[1] + size/2) - 155)
	t.goto(text_pos)    
	
	textProperties(text)

def drawNV(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(101)
	t.right(90)
	t.forward(129)
	t.right(90)
	t.forward(10)
	t.left(90)
	t.forward(12)
	t.right(135)
	t.forward(128)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 5,(location[1] + size/2) - 105)
	t.goto(text_pos)    
	
	textProperties(text)

def drawID(location, size, color, text):

	properties(color, location)
	
	t.seth(90)
	t.forward(46)
	t.left(74)
	t.forward(8)
	t.right(101)
	t.forward(32)
	t.left(71)
	t.forward(10)
	t.seth(90)
	t.forward(69)
	t.right(90)
	t.forward(18)
	t.right(90)
	t.forward(24)
	t.left(31)
	t.forward(42)
	t.right(31)
	t.forward(18)
	t.left(45)
	t.forward(38)
	t.left(45)
	t.forward(42)
	t.right(90)
	t.forward(49)  
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) - 10,(location[1] + size/2) - 25)
	t.goto(text_pos)    
	
	textProperties(text)	

def drawUT(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(56)
	t.right(90)
	t.forward(20)
	t.left(90)
	t.forward(30)
	t.right(90)
	t.forward(89)
	t.right(90)
	t.forward(86)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) - 7,(location[1] + size/2) - 115)
	t.goto(text_pos)    
	
	textProperties(text)

def drawAZ(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(86)
	t.right(90)
	t.forward(104)
	t.right(90)
	t.forward(50)
	t.right(45)
	t.forward(30)
	t.left(45)
	t.forward(25)
	t.right(90)
	t.forward(26)
	t.right(46)
	t.forward(11)
	t.left(70)
	t.forward(21)
	t.seth(90)
	t.forward(12)
	t.right(90)
	t.forward(11)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) - 7,(location[1] + size/2) - 115)
	t.goto(text_pos)    
	
	textProperties(text)

def drawMT(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(230)
	t.right(90)
	t.forward(85)
	t.right(90)
	t.forward(140)
	t.left(90)
	t.forward(19)
	t.right(90)
	t.forward(42)
	t.right(45)
	t.forward(37)
	t.right(45)
	t.forward(17)
	t.left(31)
	t.forward(42)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 70,(location[1] + size/2) - 105)
	t.goto(text_pos)    
	
	textProperties(text)

def drawWY(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(139)
	t.right(90)
	t.forward(86)
	t.right(90)
	t.forward(139)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 20,(location[1] + size/2) - 105)
	t.goto(text_pos)    
	
	textProperties(text)

def drawCO(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(139)
	t.right(90)
	t.forward(89)
	t.right(90)
	t.forward(140)
	t.end_fill()
	t.penup()
	text_pos = ((location[0] + size/2) + 20,(location[1] + size/2) - 105)
	t.goto(text_pos)    
	
	textProperties(text)

def drawNM(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(120)
	t.right(90)
	t.forward(104)
	t.right(90)
	t.forward(120)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 10,(location[1] + size/2) - 110)
	t.goto(text_pos)    
	
	textProperties(text)

def drawOK(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(140)
	t.right(90)
	t.forward(75)
	t.right(105)
	t.forward(100)
	t.right(75)
	t.forward(40)
	t.left(90)
	t.forward(43)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 38,(location[1] + size/2) - 90)
	t.goto(text_pos)    
	
	textProperties(text)

def drawTX(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(42)
	t.right(90)
	t.forward(39)
	t.left(75)
	t.forward(110)
	t.right(75)
	t.forward(30)
	t.left(25)
	t.forward(16)
	t.right(40)
	t.forward(20)
	t.right(75)
	t.forward(15)
	t.left(45)
	t.forward(60)
	t.left(45)
	t.forward(25)
	t.right(90)
	t.forward(12)
	t.right(45)
	t.forward(40)
	t.right(45)
	t.forward(3)
	t.left(45)
	t.forward(50)
	t.left(45)
	t.forward(30)
	t.right(45)
	t.forward(52)
	t.right(135)
	t.forward(50)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 18,(location[1] + size/2) - 160)
	t.goto(text_pos)    
	
	textProperties(text)

def drawKS(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(106)
	t.right(60)
	t.forward(30)
	t.right(30)
	t.forward(43)
	t.right(90)
	t.forward(121)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 10,(location[1] + size/2) - 95)
	t.goto(text_pos)    
	
	textProperties(text)

def drawNE(location, size, color, text):

	properties(color, location)
	
	t.seth(90)
	t.forward(20)
	t.left(90)
	t.forward(30)
	t.right(90)
	t.forward(42)
	t.right(90)
	t.forward(86)
	t.right(15)
	t.forward(25)
	t.right(55)
	t.forward(39)
	t.left(13)
	t.forward(22)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) - 15,(location[1] + size/2) - 25)
	t.goto(text_pos)    
	
	textProperties(text)

def drawSD(location, size, color, text):

	properties(color, location)
	
	t.seth(90)
	t.forward(70)
	t.right(90)
	t.forward(112)
	t.right(80)
	t.forward(15)
	t.right(10)
	t.forward(40)
	t.right(14)
	t.forward(21)
	t.right(90)
	t.forward(22)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 8,(location[1] + size/2) - 23)
	t.goto(text_pos)    
	
	textProperties(text)

def drawND(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(101)
	t.right(80)
	t.forward(61)
	t.right(100)
	t.forward(112)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 5,(location[1] + size/2) - 88)
	t.goto(text_pos)    
	
	textProperties(text)

def drawMN(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(40)
	t.right(45)
	t.forward(30)
	t.left(45)
	t.forward(30)
	t.right(135)
	t.forward(35)
	t.left(30)
	t.forward(40)
	t.left(65)
	t.forward(30)
	t.right(40)
	t.forward(10)
	t.right(100)
	t.forward(67)
	t.right(90)
	t.forward(37)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) - 10,(location[1] + size/2) - 118)
	t.goto(text_pos)    
	
	textProperties(text)

def drawIA(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(67)
	t.right(80)
	t.forward(20)
	t.left(35)
	t.forward(20)
	t.right(75)
	t.forward(35)
	t.right(120)
	t.forward(8)
	t.left(60)
	t.forward(56)
	t.right(71)
	t.forward(39)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) - 12,(location[1] + size/2) - 88)
	t.goto(text_pos)    
	
	textProperties(text)

def drawMO(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(57)
	t.right(60)
	t.forward(102)
	t.right(60)
	t.forward(20)
	t.right(120)
	t.forward(10)
	t.left(60)
	t.forward(63)
	t.right(90)
	t.forward(50)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) + 7,(location[1] + size/2) - 110)
	t.goto(text_pos)    
	
	textProperties(text)

def drawAR(location, size, color, text):

	properties(color, location)
	
	t.seth(0)
	t.forward(63)
	t.right(60)
	t.forward(9)
	t.right(60)
	t.forward(65)
	t.seth(270)
	t.forward(10)
	t.right(90)
	t.forward(27)
	t.right(90)
	t.forward(6)
	t.left(75)
	t.forward(8)
	t.end_fill()
	t.penup()

	text_pos = ((location[0] + size/2) - 25,(location[1] + size/2) - 90)
	t.goto(text_pos)    
	
	textProperties(text)

def drawGradient():
	 # Moving to starting location
	t.penup()
	t.goto(-383, -300)
	t.seth(90)
	t.hideturtle()

	for i in range(0,255):
		color = (255 - i, i, 0)
		t.fillcolor(color)
		t.pencolor(color)
		t.pendown()
		t.begin_fill()
		t.forward(20)
		t.right(90)
		t.forward(3)
		t.right(90)
		t.forward(20)
		t.right(90)
		t.forward(3)
		t.left(180)
		t.forward(3)
		t.left(90)
		t.end_fill()
	
	
	t.penup()
	t.goto(-384, -301)
	t.pencolor(0, 0, 0)
	t.pendown()
	t.forward(20 + 2)
	t.right(90)
	t.forward(255 * 3 + 2)
	t.right(90)
	t.forward(20 + 2)
	t.right(90)
	t.forward(255 * 3 + 2)
	t.right(180)

	# Update the screen manually:
	t.update()

salaryDict = {}

salFileHandle = open('Salaries2.txt')
salRawData = salFileHandle.readlines()
salFileHandle.close()
for line in salRawData:
	line = line.strip()
	line = line.lower()
	salStateName = str(line[:line.find(',')])
	salStateSalary = int(line[line.find(',') + 2:])
	salaryDict[salStateName] = salStateSalary

# Part 2: Importing the Cost of Living by State

# Average Monthly Cost of Living
# Source: https://www.upwardli.com/resources/new-to-america-what-is-the-average-monthly-cost-of-living-in-usa#:~:text=Again%2C%20living%20expenses%20vary%20significantly,which%20is%20%2485%2C139%20per%20year.

avgCOL = 3189
colDict = {}

colFileHandle = open('CostOfLiving.txt')
colRawData = colFileHandle.readlines()
colFileHandle.close()
for line in colRawData:
	line = line.strip()
	line = line.lower()
	colStateName = str(line[:line.find(',')])
	colStateIndex = float(line[line.find(',') + 1:])
	colDict[colStateName] = round(((colStateIndex/100) * avgCOL * 12),2) # Annual cost of living by state


# Part 3: Calculating Post-tax and Cost of Living Revenue

revenueDict = {}

for state in salaryDict:
	stateTaxRate = totalTaxRate(salaryDict[state], state)
	postTaxSalary = netIncome(state)
	annualCostOfLiving = colDict[state]
	revenue = round((postTaxSalary - annualCostOfLiving), 2)
	revenueDict[state] = revenue

# Part 4: Ordering the States by Economic Viability

sortedRevenueList = []
sortedStates = []

for state in revenueDict:
	sortedRevenueList.append(revenueDict[state])

sortedRevenueList = sorted(sortedRevenueList)

for revenue in sortedRevenueList:
	for (state, value) in revenueDict.items():
		if value == revenue:
			sortedStates.append(state)
			break

# Part 5: Calculating RGB Values by State

min_revenue = min(revenueDict.values())
max_revenue = max(revenueDict.values())

for state in revenueDict:
    revenueDict[state] -= min_revenue
    revenueDict[state] /= ((max_revenue - min_revenue) / 255)
    revenueDict[state] = int(revenueDict[state])

greenList = sorted(revenueDict.values())
redList = []

for greenValue in greenList:
	redValue = round((255 - greenValue), 2)
	redList.append(redValue)

# Part 6: Drawing the States and Filling with Calculated Color

s = t.getscreen()
turtle = t.Turtle()
window_width = 1000
window_height = 800
t.setup(window_width, window_height)
t.speed(200)
t.tracer(0) # From turtle documentation: Needed to instantly draw all states
turtle.hideturtle()
turtle.penup()
t.colormode(255) # Sets up turtle to take color inputs as RGB values

# Function Calls to Draw States with Appropriate Color

drawWA((-480,310), 100, (redList[sortedStates.index("washington")],greenList[sortedStates.index("washington")], 0), "WA")
drawOR((-480,310), 100, (redList[sortedStates.index("oregon")],greenList[sortedStates.index("oregon")], 0), "OR")
drawCA((-480,223), 100, (redList[sortedStates.index("california")],greenList[sortedStates.index("california")], 0), "CA")
drawNV((-410,223), 100, (redList[sortedStates.index("nevada")],greenList[sortedStates.index("nevada")], 0), "NV")
drawID((-360,223), 100, (redList[sortedStates.index("idaho")],greenList[sortedStates.index("idaho")], 0), "ID")
drawUT((-308,223), 100, (redList[sortedStates.index("utah")],greenList[sortedStates.index("utah")], 0), "UT")
drawAZ((-308,113), 100, (redList[sortedStates.index("arizona")],greenList[sortedStates.index("arizona")], 0), "AZ")
drawMT((-342,376), 100, (redList[sortedStates.index("montana")],greenList[sortedStates.index("montana")], 0), "MT")
drawWY((-251,290), 100, (redList[sortedStates.index("wyoming")],greenList[sortedStates.index("wyoming")], 0), "WY")
drawCO((-221,203), 100, (redList[sortedStates.index("colorado")],greenList[sortedStates.index("colorado")], 0), "CO")
drawNM((-221,113), 100, (redList[sortedStates.index("new mexico")],greenList[sortedStates.index("new mexico")], 0), "NM")
drawOK((-100,113), 100, (redList[sortedStates.index("oklahoma")],greenList[sortedStates.index("oklahoma")], 0), "OK")
drawTX((-100,103), 100, (redList[sortedStates.index("texas")],greenList[sortedStates.index("texas")], 0), "TX")
drawKS((-81,183), 100, (redList[sortedStates.index("kansas")],greenList[sortedStates.index("kansas")], 0), "KS")
drawNE((-81,183), 100, (redList[sortedStates.index("nebraska")],greenList[sortedStates.index("nebraska")], 0), "NE")
drawSD((-111,245), 100, (redList[sortedStates.index("south dakota")],greenList[sortedStates.index("south dakota")], 0), "SD")
drawND((-111,376), 100, (redList[sortedStates.index("north dakota")],greenList[sortedStates.index("north dakota")], 0), "ND")
drawMN((-9,376), 100, (redList[sortedStates.index("minnesota")],greenList[sortedStates.index("minnesota")], 0), "MN")
drawIA((5,261), 100, (redList[sortedStates.index("iowa")],greenList[sortedStates.index("iowa")], 0), "IA")
drawMO((11,203), 100, (redList[sortedStates.index("missouri")],greenList[sortedStates.index("missouri")], 0), "MO")
drawAR((41,105), 100, (redList[sortedStates.index("arkansas")],greenList[sortedStates.index("arkansas")], 0), "AR")

t.tracer(0) # From turtle documentation: Needed to instantly draw all states
drawGradient()


t.mainloop() # DO NOT TOUCH

# Reference Map Link: https://www.istockphoto.com/vector/simple-map-of-american-50-states-in-the-united-states-vector-illustration-gm1349117213-425845536

# Part 7: Displaying Economic Viability and Profit Using Bar Graph
'''
colors = [] # Initializing color list

for colorIndex in range(len(sortedStates)):
    red = redList[colorIndex] / 255  # Normalize red value to 0-1 range
    green = greenList[colorIndex] / 255  # Normalize green value to 0-1 range
    colors.append((red, green, 0))

plt.figure(figsize = (12, 8))
plt.title('Annual Profit by State')
plt.bar(sortedStates, sortedRevenueList, color = colors, width = 0.6)

# Label Formatting
plt.xlabel('States')
plt.ylabel('Annual Profit ($/yr)')

# Improve Readability
plt.xticks(rotation = 90) # Makes all state names vertical
plt.subplots_adjust(bottom = 0.2) # Adjusts vertical compression of graph

# Display the graph
plt.show()
'''




