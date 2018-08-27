from sys import stdin

def calculaterDist(startCity,endCity,mLines):


vInput = [ x.strip() for x in stdin]
firstLine = vInput[0]
# firstLine = '3 2 1'
n,m,q = [ int(x) for x in firstLine.split() ]

#For debug
# n,m,q = [ 10,13,5]
mLines = vInput[1:m+1]
#For debug
# mLines = ['1 2 3', '2 3 2', '3 1 10', '4 1 5', '3 4 7', '10 3 2', '6 10 1', '6 7 8', '5 7 7', '5 6 4', '7 8 6', '8 9 9', '9 5 1']
qLines = vInput[m+1:]
#For debug
# qLines = ['1 8', '3 1', '9 10', '5 2', '4 6']

#parse QLine

for line in qLines:
    startCity, endCity = line.split()
    distance = calculaterDist(startCity,endCity,mLines)
    print(distance)



