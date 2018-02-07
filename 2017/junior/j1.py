from sys import stdin

def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList    
    
vinput=readInput()
#print(vinput)
# vinput=['100','-100']
x=int(vinput[0])
y=int(vinput[1])
if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
else: 
    print(3)