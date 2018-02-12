# CCC Junior 5: Assigning Partners
#
# Array inverse checking (The idea is for all positions i
# in array A, find the position of B[i] in A, call it j.
# Now A[i] should equal B[j].)
#
# The problem is made easy because the input lines
# are guaranteed to have N DIFFERENT names, so no checks
# for duplicates or missing names need occur and the second
# line has the SAME names as the first, so no checks needed
# for 'not found' conditions.
#
from sys import stdin
# vInput=[ x.strip() for x in stdin]
vInput=['4','Ada Alan Grace John','John Grace Alan Ada']
vInput=['7','Rich Graeme Michelle Sandy Vlado Ron Jacob','Ron Vlado Sandy Michelle Rich Graeme Jacob']
n=int(vInput[0])
first=vInput[1].split()
second=vInput[2].split()


# for each position i, it must be the case that
# first [i] = second[position in first of second[i]]
# (ie. a to b is also b to a)
# and that position in first of second[i] not = i
# (ie. a to a is not the case)

i = 0
state = "good"
# while i < n and state == "good":
#     position = first.index(second[i])
#     if first[i] != second[position] or position == i:
#         state = "bad"
#     i = i + 1
while i<n and state =='good':
    if (first[i] == second[i]):
        state ='bad'
    else:
        if  second[i] in first:
            position = first.index(second[i])
            if first[i] != second[position] :
                state='bad'
        else:
            state='bad'
    i=i+1
print(state)
    
    
