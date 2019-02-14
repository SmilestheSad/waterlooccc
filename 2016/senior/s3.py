#

#Read input

def findStartM(mList,nexHopsDict):
    mStart = mList[0]
    for m in mList:
        if len(nexHopsDict[m]) == 1:
            mStart = m
            break
    return mStart

def nextHops(mNumber,pList):
    nextHopList = []
    for p in pList:
        if mNumber in p:
            nextHop = ''.join(p).replace(mNumber,'')
            nextHopList.append(nextHop)

            #find possible path
    return nextHopList

def mInNexHops(mList,nexHops):
    mNumber = ''
    findFlag = False
    for m in mList:
        if m in nexHops:
            mNumber = m
            findFlag = True
            break
    
    return mNumber,findFlag


def buildNextHops(l):

    nexHopsDict = dict()
    for s in l:
        print(s[0],s[1])
        v1 = nexHopsDict.get(s[0],[])
        v1.append(s[1])
        v2 = nexHopsDict.get(s[1],[])
        v2.append(s[0])

        # nexHopsDict[s[0]] = v1.append([s[1]])
        nexHopsDict[s[0]] = v1
        nexHopsDict[s[1]] = v2
    # print(l) 
    return nexHopsDict    
            


n,m = list(map(int,input().split()))
mList = input().split()
pathList = []
for s in range(n-1):
    pathList.append(input().split())

nextHopDict = buildNextHops(pathList)
#Find Start M house (least next hops)
mStart = findStartM(mList,nextHopDict)

#
print(mStart)

