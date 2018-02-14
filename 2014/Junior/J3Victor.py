from sys import stdin 
vInput = [x.strip() for x in stdin]
david = 100
antonia = 100
n = int(vInput[0])
rlist = vInput[1:]
for i in range(n): 
    roll = rlist[i].split()
    a = int(roll[0])
    d = int(roll[1])
    if a < d:
        antonia = antonia - d
    elif d < a:
        david = david - a 
print(david)
print(antonia)