######## Number shift 2017 J2#######
def shiftNumber(base, shift):
    # Traditional way
    # total=0
    # if shift > 0:
    #     for i in range(shift+1):
    #         total = total + base*10**i
    # else:
    #     total=base
    # Smart way
    total = sum([base*10**i for i in range(shift+1)])
    return total


print(shiftNumber(12, 3))

# Get factor list


def getFactor(n):
    factorList = [1, n]
    # for i in range(2, n):
    #     if (n % i == 0):
    #         factorList.append(i)
    factors = [ x for x in range(2,n) if (n%x == 0)]
    return factorList + factors
print(getFactor(124))


def isPrime(n):
    result = True
    if (n == 2 or n == 3):
        result = True
    if (n > 3):
        for i in range(2, n):
            if (n % i == 0):
                result = False
                break
    return result
# print(isPrime(240))


# Calculate point1(x1,y1) and point2 (x2,y2) distance - 2017 J3
def twoPointDistance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

# Convert clock string to mins after midnight. 2017-J4


def clockString2Mins(s):
    # s = '1:28'
    hours, mins = int(s.split(':')[0]),    int(s.split(':')[1])
    minsOfDay = hours*60 + mins
    return minsOfDay
# print(clockString2Mins('2:38'))

###### convert mins after midnight back to clock#######


def mins2Clock(mins):
    # mins = 90
    hours, mins = mins//60, mins % 60
    clockString = "%02d:%02d" % (hours, mins)
    return clockString
# print(mins2Clock(90))


# Combination (order doesn't matter. It means less) and permutations (order does matter. it means more)
import math


def combinationNumber(n, r):
    # n!/((n-r)! * r!)
    return int(math.factorial(n)/(math.factorial(n-r) * math.factorial(r)))


def permutationsNumber(n, r):
    # n!/(n-r)!
    return int(math.factorial(n)/math.factorial(n-r))
# print(combinationNumber(4,3),permutationsNumber(4,3))


from itertools import permutations,combinations,product

# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
# permutations(range(3)) --> 012 021 102 120 201 210
var1 = list(permutations('ABCD',2))


# combinations('ABCD', 2) --> AB AC AD BC BD CD
# combinations(range(4), 3) --> 012 013 023 123
var2 = list(combinations('ABCD',2))


# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
var3 = list(product('ABCD', 'xy'))



# Data Set sort,unique and count
from collections import Counter

c = Counter("aaabbdddccceee")
print(c.most_common())  # [('c', 3), ('a', 3), ('d', 3), ('e', 3), ('b', 2)]
c = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(c.most_common())  # [('blue', 3), ('red', 2), ('green', 1)]

c = Counter([1, 3, 1, 4, 4, 5, 5, 5])
print(c.most_common())  # [(5, 3), (1, 2), (4, 2), (3, 1)]
print(c.most_common()[0][0], c.most_common()[0][1])  # Top occurence and count
print(c.most_common()[-1][0], c.most_common()[-1][1])  # Bottom occurence and count

# Common counter method
var1 = list(c.keys())  # convert counter element to unique list  [1,3,4,5]
var2 = list(c.values())  # convert counter element to unique list  [2,1,2,3]
var3 = dict(c)  # convert to dict {1: 2, 3: 1, 4: 2, 5: 3}
