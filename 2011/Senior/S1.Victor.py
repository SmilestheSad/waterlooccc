from sys import stdin
def readInput():
    inputList = []
    for line in stdin:
        inputList.append(line.strip())
    return inputList
vInput = readInput()
# vInput = ['3','The red cat sat on the mat.','Why are you so sad cat?','Don’t ask that.']
inputList1 = vInput[1:]


tcount,Tcount,scount,Scount = 0,0,0,0


for i in range(len(inputList1)):
    astring = inputList1[i]
    tcount = astring.count('t') + tcount
    Tcount = astring.count('T') + Tcount
    scount = astring.count('s') + scount
    Scount = astring.count('S') + Scount

if (tcount + Tcount) > (scount + Scount):
    print('English')
elif (tcount + Tcount) < (scount + Scount):
    print('French')
else :
    print('French')