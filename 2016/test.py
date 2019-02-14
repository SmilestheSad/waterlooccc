from math import log
def nextgens(T):
  gens = 1<<int(log(T,2))
  if gens > T:
    gens /= 2
  return int(gens)

def nextgensNew(T):
    b = len(str(bin(T)))
    res = 2**(b-3)
    return res

T = 15
while T > 0:
  gens = nextgens(T)
  T -= gens
  print(gens,15,T)
#   generations(gens,N)
#   newgen,oldgen = oldgen,newgen