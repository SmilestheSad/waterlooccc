from itertools import permutations,combinations,product

# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
# permutations(range(3)) --> 012 021 102 120 201 210
var1 = list(permutations('ABCD',2))
var4= list(permutations([1,3,5,7],2))

# combinations('ABCD', 2) --> AB AC AD BC BD CD
# combinations(range(4), 3) --> 012 013 023 123
var2 = list(combinations('ABCD',2))


# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
var3 = list(product('ABCD', 'xy'))

print(var1)