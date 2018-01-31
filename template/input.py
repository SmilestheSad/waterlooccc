from sys import stdin

def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList    

def readInput1():
    inputList = []
    while True:
        try:
            line = input()
            inputList.append(line.strip())
        except EOFError:
            return inputList
            break
           

def readFile(filename):
    f = open(filename, 'r')
    inputList = f.read().splitlines()
    return inputList

#Option 1
#vInput = readInput() 
vInput= ['1 2 3 4', '9 4 5 6', '8 4 5 6', '0 4 5 6'] 
#Option 2
#vInput = readFile('input.txt')
#Option 3
#vInput = readInput1()
print(vInput)   # vInput= ['1 2 3 4', '9 4 5 6', '8 4 5 6', '0 4 5 6'] 
vFirstLine=vInput[0]
vFirstStringFromFirstLine = vInput[0].split()[0]
print(vFirstLine,"\n",vFirstStringFromFirstLine)

vInputNew = [ x.split() for x in vInput ]
vInputNew1 = [ int(x) for y in vInputNew for x in y]

vIntList = []
for x in vInput:  # x = '1 2 3 4' or '9 4 5 6' ...
    vRowList = []
    for y in x.split():  # split x from string into a string list
        vRowList.append(int(y))  # convert to int and append to row list
    vIntList.append(vRowList)   # Append finished row list to final list

print(vIntList)        


print(vInputNew1)

