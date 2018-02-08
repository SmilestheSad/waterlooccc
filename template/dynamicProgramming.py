#  Bottom-Up : 
#  Analyze the problem and see the order in which the sub-problems are solved and start solving from the trivial subproblem, 
#  up towards the given problem. In this process, 
#  it is guaranteed that the subproblems are solved before solving the problem. 
#  This is referred to as Dynamic Programming.

# Fibonacci
# 0,1,1,2,3,5,8,13,21...
# F(0)=0 ; F(1) = 1; F(N)=F(N-1)+F(N-2) 

def fib(n):
    
    if (n==0):
        return 0
    if (n==1):
        return 1
    return fib(n-1)+fib(n-2)

l=[]
for i in range(9):
    l.append(fib(i))
print(l)  #[0, 1, 1, 2, 3, 5, 8, 13, 21]    


# Pascal Triangel
#             1
#          1    1
#        1    2   1
#      1   3    3   1
#    1   4   6    4   1
#  1  5   10  10   5   1 
# C(n,m) = C(n-1,m) + C(n-1,m-1)


def pascalT(n,m):
    if n == 1 or m == 1 or m==n:
        return 1
    return pascalT(n-1,m) + pascalT(n-1,m-1)


print(pascalT(6,3))  # 10
print(pascalT(5,2))  # 4

