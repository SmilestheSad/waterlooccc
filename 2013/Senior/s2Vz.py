def check(x):
    if sum(x) > max:
        return False
    else:
        return True
max = int(input())
n = int(input())
x = list()
trains = 4
yeet = True
for i in range(4):
    x.append(int(input()))
    if sum(x) > max and i == 0:
        smiles = (i,)
        yeet == False
    elif sum(x) > max:
        smiles = (i+1,)
        yeet == False
    else:
        continue
if yeet == True:
    for i in range(n):
        x.append(int(input()))
        x.pop(0)
        if check(x) == True:
            trains+=1
        elif check(x) == False:
            print(trains)
            break
else:
    print(smiles[0])


