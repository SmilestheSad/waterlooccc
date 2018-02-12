#https://dmoj.ca/problem/nccc5j2

from sys import stdin
from collections import Counter  # useful for sort,group/unique,count
from statistics import mean,median_high,median_low,median,mode


#vInput= [ x.strip() for x in stdin]
vInput = ['4','1 1 2 2 ']
aList=[ int(x) for x in vInput[1].split() ]
c= Counter(aList).most_common()
mostCount=c[-1][1]

newList=[]
for i in range(len(c)):
    if c[i][1] == mostCount:
        newList.append(c[i][0])

print(min(newList))
# print(median(aList))  #3.0
# print(median_low(aList))  #2
# print(median_high(aList))  #2

