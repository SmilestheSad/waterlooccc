from sys import stdin


def readInput():
    inputList = []
    for line in stdin:
        inputList.append(line.strip())
    return inputList


vInput = readInput()
#vInput=['10 2','10 4','5']
print(vInput)
steps = int(vInput[2])
startPoint = vInput[0].split()
endPoint = vInput[1].split()

# Calculate distance
result = 'N'
xDistance = abs(int(startPoint[0]) - int(endPoint[0]))
yDistance = abs(int(startPoint[1]) - int(endPoint[1]))
totalDistance = xDistance + yDistance
if (steps < totalDistance):
    result = 'N'
elif ((steps - totalDistance) % 2 == 0):
    result = 'Y'
else:
    result = 'N'

print(steps, totalDistance, result)
