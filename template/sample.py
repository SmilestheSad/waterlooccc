# Import and readinput function
from sys import stdin
from collections import Counter  # useful for sort,group/unique,count
from math import sqrt, factorial, ceil,floor,
from statistics import mean,median,median_high,median_grouped,median_high,mode


#Put input into a list
vInput = [ x.strip() for x in stdin]
#vInput = ['3','6','3 5 7 8','6 9 34 1']

#Process Input VAR
inputVar1 = vInput[0]
inputVar2 = int(vInput[1])
inputList1 = vInput[2:]   # ['3','5','7','8']
inputList1 = [int(x) for x in inputList1.split()].sort()
intList2 = [ int(x) for x in vInput[2:] if ( int(x)%2 == 0 )]

#Create initial variable for output
total,someState,count = 0,1,0
newList=[]  # create new list to hold processed elements
result="something" # default result string
resultFlag = True  # Default boolean, pick most likely one and overwrite in below logic code

#Main Code
def doSomething(hour,mins): # x is hour and y is mins
    clockString = "%02d:%02d" % (hour,mins)
    return clockString   # 03:24

for i in range(inputVar2):
    total = total + i**2
    if ( inputList1[i] > 0 ):  # some condition is true
        newList.append()
        resultFlag = False
        count = count + 1
    else:
        hour=i
        mins=i
        doSomething(hour,mins)

#Post Processing new List if necessary
newList.sort()
finalResult = sum(newList)
finalResult = max(newList)  # min(L), len(L)
# Group and Count for newList or a string
# IMPORTANT:  "from collections import Counter"
counterList = Counter(newList)  # 
c = counterList.most_common()   # Example [(5, 3), (1, 2), (4, 2), (3, 1)]   - (vaule, count) List
topOccurence = c[0][0]  # Top occurence and count
topCount =  c[0][1] # Top count
bottomOccurence = c[-1][0]
bottomCount = c.most_common()[-1][1])  # Bottom occurence and count
# Common counter method
var1 = list(counterList.keys())  # convert key to unique list  [1,3,4,5]
var2 = list(counterList.values())  # convert value to unique list  [2,1,2,3]
var3 = dict(c)  # convert to dict {1: 2, 3: 1, 4: 2, 5: 3}



#Print Output if it's not printed inside loop
print(finalResult)

