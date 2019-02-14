from collections import Counter


s = "abbcccdddd"
c = Counter(s)   # Counter({'d': 4, 'c': 3, 'b': 2, 'a': 1})

#Create
c= Counter(a=1,b=2,c=3,d=4)
#Delete
del c['d']                      # Delete d
#Update
c['d'] = 4                      # Add d:4 back
# c.clear()                       # reset all counts
#R(ead)
# Type Convert
list(c)                         # list unique elements ['a', 'b', 'c', 'd']
set(c)                          # convert to a set {'a', 'b', 'd', 'c'}
dict(c)                         # convert to a regular dictionary {'a': 1, 'b': 2, 'c': 3, 'd': 4}
cList = c.most_common()  # [('d', 4), ('c', 3), ('b', 2), ('a', 1)]
c['d']  # 4
mostFrequentLetter = cList[0][0]  # d
leastFrequentCount = cList[-1][1]
sum(c.values())                 # total of all counts 10




def listAlistB(a,b):
    '''
    return (sUnion,sIntersection,sDiffA,sDiffB)
    '''
    # aLen,bLen = len(a),len(b)
    setA,setB = set(a),set(b)
    # setALen,setBLen = len(setA),len(setB)
    sUnion = setA.union(setB)
    sIntersection = setA.intersection(setB)
    sDiffA = setA.difference(setB)   # similar to setA - setB
    sDiffB = setB.difference(setA)   # 

    return (sUnion,sIntersection,sDiffA,sDiffB)


a = [1,2,3,4,5]
b = [3,4,5,6,7]
print(listAlistB(a,b))


set(a) - set(b)
# ({1, 2, 3, 4, 5, 6, 7}, {3, 4, 5}, {1, 2}, {6, 7})