# To get STDIN
# Option1: From WINDOW Command Prompt or Visual Studio Code Terminal window
# cd <directoryname>
# type <inputfilename> | python <yourpython.py>
#
# Option2: From STDIN keyboard
# python <yourpython.py>
# type input and enter...... <Control>+<Z> followed by <Enter> ends input


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

vInput = readInput() 
print(vInput)   

#Sample Input input1.txt 2016/J2
# 1 2 3 4
# 9 4 5 6
# 8 4 5 6
# 0 4 5 6
# vInput= ['1 2 3 4', '9 4 5 6', '8 4 5 6', '0 4 5 6'] 
# vInput=[ x.split() for x in vInput]  <- convert each element to list to become list inside list


# Sample Input input2.txt 2016/J5
# First line is question either 1 or 2
# Second line is number of person N
# Third line contain N space separated integer : the speed of each person from country A
# Four line contain N space separated integer : the speed of each person from country A
# 1
# 3
# 5 1 4
# 6 2 4
# vInput = readInput()  
# vInput = ['1','3','5 1 4','6 2 4']
# vQuestion = vInput[0]
# vPersonCount = int(vInput[1])
# vCountry1Speed = [ int(x) for x in vInput[2].split() ]
# vCountry2Speed=  [ int(x) for x in vInput[3].split() ]

# Sample input3.txt 2013 J4
# First line represent T is total number of minutes available
# Second line is number of tasks
# Starting from third line, it's mins required for each tasks
# 6
# 3
# 3
# 6
# 3
# t = int(vInput[0])
# c = int(vInput[1])
# timeList = [int(x) for x in vInput[2:]]
# timeList.sort()  

