from itertools import combinations

a = [1,5,3,4,2]
# b = list(combinations(a,2))
# print(b)
# res= 0

n =len(a)
k= 2
for x in range(n):
    count=0
    for y in range(x+1,n):
        if abs(a[x]-a[y]) == k:
            count +=1

print(count)


