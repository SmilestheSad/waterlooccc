# https://dmoj.ca/problem/nccc5j3s1
from sys import stdin
from statistics import median
import itertools 


vInput = [x.strip() for x in stdin]
#vInput=['4 1','1 1 2 2']
n=int(vInput[0].split()[0])
x=int(vInput[0].split()[1])
vList = [ int(x) for x in vInput[1].split() ]

vCombination = list(itertools.combinations(vList,3))
count=0
for l in vCombination:
    if median(l) == x:
        print(l)
        count = count + 1



print(count)



