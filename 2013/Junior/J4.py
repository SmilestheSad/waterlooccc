# CCC 2013 Junior 4: Time on Task

# Problem Description
# You have been asked by a parental unit to do your chores.
# Each chore takes a certain amount of time, but you may not have enough time to do all of your
# chores, since you can only complete one chore at a time. You can do the chores in any order that
# you wish.
# What is the largest amount of chores you can complete in the given amount of time?
# Input Specification
# The first line of input consists of an integer T (0 ≤ T ≤ 100000), which is the total number of
# minutes you have available to complete your chores.
# The second line of input consists of an integer C (0 ≤ C ≤ 100), which is the total number
# of chores that you may choose from. The next C lines contain the (positive integer) number of
# minutes required to do each of these chores. You can assume that each chore will take at most
# 100000 minutes.
# Output Specification
# The output will be the maximum number of chores that can be completed in time T.

vInput = ['6', '3', '3', '6', '3']
vInput = ['6', '5', '5', '4', '3','2','1']
t = int(vInput[0])
c = int(vInput[1])
timeList = [int(x) for x in vInput[2:]]
timeList.sort()  # small to big order

sum = 0
for i in range(c):
    sum = sum + timeList[0]
    if ( sum < t):
        continue
    else:
        print(i+1)
        break    