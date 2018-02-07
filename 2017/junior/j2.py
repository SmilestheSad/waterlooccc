from sys import stdin

def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList    
vinput = ['12','4']
#vinput=readInput()


base=int(vinput[0])
shift=int(vinput[1])


total=0  
if shift > 0:
    for i in range(0,shift+1):
        total = total + base*10**i
    print(total)
else:
    print(base)
    
