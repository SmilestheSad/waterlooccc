from sys import stdin
#Read Input Function

def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList
vInput = readInput()    
month = int(vInput[0])
day = int(vInput[1])
if month == 2 and day == 18:
    print("Special")
elif month < 2 or (month == 2 and day < 18):
    print("Before")
else: 
    print("After")