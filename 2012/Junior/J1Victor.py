# Import and readinput function
from sys import stdin
def readInput():
    inputList = []
    for line in stdin:
        inputList.append(line.strip())
    return inputList
speedinput = int(input('Enter the speed limit'))
recordingspeed = int(input('Enter the recorded speed of the car'))
if speedinput > recordingspeed:
    print('youre fine')
else:
    if (recordingspeed - speedinput) >=1 and (recordingspeed - spee)
