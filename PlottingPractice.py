import matplotlib.pyplot as plt

def readData(filename):
    regions = []
    food = []
    fileHandle = open(filename)
    rawData = fileHandle.readlines()
    for line in rawData:
        print(line)
        first, second = line.split(",") # The "delimeter" is the comma (what the line is separated by)
        regions.append(first)
        food.append(int(second))

    return regions, food

regions, food = readData('Food.txt')

# Boiler Plate Plotting in General
plt.plot(food,'bx') # plt.plot(data, 'Color, Line Style, Marker Shape')
plt.xlabel("Regions")
plt.ylabel("Food per Capita per Year (kg)")
plt.title("Food Consumed by Region")

# Advanced Plotting
ticks = range(0,len(regions))
plt.xticks(ticks,regions, rotation = 270)

# Saving and Firing
# plt.savefig("plot.png")
plt.show()

# Customization documentation link: 
# https://camo.githubusercontent.com/023e95270f8b361d49e5001684dfb87fd283bba9354f4c7c1921155ced173c67/68747470733a2f2f6d6174706c6f746c69622e6f72672f63686561747368656574732f63686561747368656574732d312e706e67
# https://matplotlib.org/stable/api/pyplot_summary.html

