# https://dmoj.ca/problem/ccc04s2

vInput=['5 2','99 97 100 85 -4','95 97 100 62 1000']
k=int(vInput[0].split()[1])
n=int(vInput[0].split()[0])
scoreList=vInput[2:]

for i in range(k):
    aList = [ int(x) for x in scoreList[i].split() ]
    aSortList = aList[:].sort(reverse=True)

