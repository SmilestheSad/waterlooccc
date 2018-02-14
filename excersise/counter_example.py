from collections import Counter


s = "abbcccdddd"
c = Counter(s)   # Counter({'d': 4, 'c': 3, 'b': 2, 'a': 1})

#Create
c= Counter(a=1,b=2,c=3,d=4)
#Delete
del c['d']                      # Delete d
#Update
c['d'] = 4                      # Add d:4 back
c.clear()                       # reset all counts
#R(ead)
# Type Convert
list(c)                         # list unique elements ['a', 'b', 'c', 'd']
set(c)                          # convert to a set {'a', 'b', 'd', 'c'}
dict(c)                         # convert to a regular dictionary {'a': 1, 'b': 2, 'c': 3, 'd': 4}
c.most_common()  # [('d', 4), ('c', 3), ('b', 2), ('a', 1)]
c['d']  # 4
mostFrequentLetter = cList[0][0]  # d
mostFrequentCount = cList[-1][1]
sum(c.values())                 # total of all counts 10


# Math for counter object
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
# add two counters together:  c[x] + d[x]  = Counter({'a': 4, 'b': 3})
cAdd = c + d
# subtract (keeping only positive counts) = Counter({'a': 2})
cSubtract = c - d
# intersection:  min(c[x], d[x]) = Counter({'a': 1, 'b': 1})
cMin = c & d
# union:  max(c[x], d[x]) Counter({'a': 3, 'b': 2})
cMax = c | d

print(c)
