
from sys import stdin
def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList    

def button1(l,n):
    for i in range(n):
        number=l[0]
        del l[0]
        l.append(number)
    return l
def button2(l,n):
    for i in range(n):
        number=l[-1]
        l.pop()
        l.insert(0,number)
    return l
def button3(l,n):
    for i in range(n):
        first =l[0]
        second = l[1]
        l[0] = second
        l[1] = first
    return l
        

vInput=readInput()
#vInput=['2','1','3','1','2','3','4','1']
vCommandList=[]
vRepeatList=[]
for i in range(len(vInput)):
    if ( i % 2 == 0):
        vCommandList.append(int(vInput[i]))
    else:
        vRepeatList.append(int(vInput[i]))    

playList = ['A','B','C','D','E']
for i in range(len(vCommandList) - 1 ):
    if ( vCommandList[i] == 1):
        playList = button1(playList,vRepeatList[i])
    elif vCommandList[i] == 2:
        playList = button2(playList,vRepeatList[i])
    elif vCommandList[i] == 3:
        playList = button3(playList,vRepeatList[i])
    else:
        break  

print(' '.join(playList))        




