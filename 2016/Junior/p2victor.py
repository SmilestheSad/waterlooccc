from sys import stdin
def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList    
vInput=['16 3 2 13','5 10 11 8','9 6 7 12','4 15 24 1']
#vInput=readInput()

vInput=[x.split() for x in vInput]

basetotal = int(vInput[0][0]) + int(vInput[0][1]) + int(vInput[0][2]) + int(vInput[0][3])
result = "magic"


for i in range(4):
    rowtotal= int(vInput[i][0]) + int(vInput[i][1]) + int(vInput[i][2]) + int(vInput[i][3])
    columntotal= int(vInput[0][i]) + int(vInput[1][i]) + int(vInput[2][i]) + int(vInput[3][i])
    if rowtotal != basetotal or columntotal != basetotal:
        result="not magic"
print(result)
