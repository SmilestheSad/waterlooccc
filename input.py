from sys import stdin
def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList    

def readFile(filename):
    f = open(filename, 'r')
    inputList = f.read().splitlines()
    return inputList

#Option1
#vInput = readInput()  
#Option2
vInput = readFile('input.txt')
print(vInput)   