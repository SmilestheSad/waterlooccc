from math import log
import sys
input = sys.stdin.readline

#credit to https://amorim.ca/display/CS/Circle+of+Life

# N,T = map(int,input().split())
# oldgen = list(map(int,list(input().strip('\n'))))

T,N=15,15
oldgen =list(map(int,list('100010010111001'.strip('\n'))))




newgen = [False for x in range(N)]



#Get highest binary bits of T. return: 4 if T=4,5,6,7,  8 if T=8,9,10,11,12,13,14,15
def nextgens(T):
  gens = 1<<int(log(T,2))
  if gens > T:
    gens /= 2
  return int(gens)

#
def cell(ind,N):
  ind = ind%N
  if ind < 0:
    return ind+N
  else:
    return ind

def generations(T,N):
  for i in range(N):
    newgen[i] = oldgen[cell(i-T,N)]^oldgen[cell(i+T,N)]
    
while T > 0:
  gens = nextgens(T)
  T -= gens
  generations(gens,N)
  newgen,oldgen = oldgen,newgen
  print('T:',T,gens,''.join(str(x) for x in oldgen),''.join(str(x) for x in newgen))

print (''.join(str(x) for x in oldgen))