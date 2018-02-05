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

#Sample Input input1.txt
# 1 2 3 4
# 9 4 5 6
# 8 4 5 6
# 0 4 5 6
# > type input1.txt | python input.py
vInput = readInput() 
print(vInput)   # vInput= ['1 2 3 4', '9 4 5 6', '8 4 5 6', '0 4 5 6'] 
#Use below for debug and development
vInput= ['1 2 3 4', '9 4 5 6', '8 4 5 6', '0 4 5 6'] 

#Sample Input input2.txt
# First line is question either 1 or 2
# Second line is number of person N
# Third line contain N space separated integer : the speed of each person from country A
# Four line contain N space separated integer : the speed of each person from country A
# 1
# 3
# 5 1 4
# 6 2 4
vInput = readInput()  # vInput = ['1','3','5 1 4','6 2 4']
vQuestion=vInput[0]
vPersonCount=int(vInput[1])
vCountry1Speed= vInput[2].split()
vCountry2Speed= vInput[3].split()

# vFirstLine=vInput[0]
# vFirstStringFromFirstLine = vInput[0].split()[0]
# print(vFirstLine,"\n",vFirstStringFromFirstLine)

# vInputNew = [ x.split() for x in vInput ]
# vInputNew1 = [ int(x) for y in vInputNew for x in y]

# vIntList = []
# for x in vInput:  # x = '1 2 3 4' or '9 4 5 6' ...
#     vRowList = []
#     for y in x.split():  # split x from string into a string list
#         vRowList.append(int(y))  # convert to int and append to row list
#     vIntList.append(vRowList)   # Append finished row list to final list

# print(vIntList)        


# print(vInputNew1)

