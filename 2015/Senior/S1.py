# CCC 2015 Senior 1: Zero That Out
#
# A list processing problem (using a stack)
#
# Python's append() - add to the end of the list
#      and pop() - remove the last item
# make this an easy problem


# file = open("s1.5.in", "r")
# k = int(file.readline())
vInput = ['4', '3', '0', '3', '0']
vInput = ['10','1','3','5','4','0','0','7','0','0','6']

k = int(vInput[0])
inputList = [int(x) for x in vInput[1:]]
newList = []
for i in inputList:
    if i == 0:
        newList.pop()
    else:
        newList.append(i)


print(sum(newList))
