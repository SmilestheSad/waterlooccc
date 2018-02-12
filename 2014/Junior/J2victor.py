from sys import stdin
def readInput():
    inputList = []
    for line in stdin:
        inputList.append(line.strip())
    return inputList
# vInput = ['6','ABAAAAAAABBBBBBB']
vInput = readInput()
amount = vInput[0]
votes = vInput[1]
aAmount = votes.count('A')
bAmount = votes.count('B')
if aAmount > bAmount:
    print('A')
elif bAmount > aAmount:
    print('B')
else:
    print('Tie')