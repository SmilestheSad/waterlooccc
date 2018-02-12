# CCC 2014 Junior 4: Party Invitation
#
# relatively straight forward 1D array processing
# (element removal and modulo arithmetic)
#
from sys import stdin

#vInput=[x.strip() for x in stdin]

vInput=['10','2','2','3']

k=int(vInput[0])
m=int(vInput[1])
roundList=list(map(int,vInput[2:]))
friendList=list(range(1,k+1))

for i in range(m):
    newList=[]
    removeR=roundList[i]
    for j in range(len(friendList)):
        if (j+1) % removeR != 0:
            newList.append(friendList[j])
    friendList = newList[:]        


for f in friendList:
    print(f)
