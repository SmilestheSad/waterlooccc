# Import and readinput function
from sys import stdin
def readInput():
    inputList = []
    for line in stdin:
        inputList.append(line.strip())
    return inputList
vInput = readInput()
# vInput = ['How are you :-) doing :-( today :-)?']
happysadstring=vInput[0]
happyamount = happysadstring.count(':-)')
sadamount = happysadstring.count(':-(')
if happyamount > 0 or sadamount > 0:
    if happyamount == sadamount:
        print('unsure')
    elif happyamount > sadamount:
        print('happy')
    else:
         print('sad')
else:
    print('none')