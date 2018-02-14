from sys import stdin
vInput = [x.strip() for x in stdin]
ppl = int(vInput[0])
pair1 = vInput[1].split()
pair2 = vInput[2].split()
result = 'good'
for i in range(ppl):
    if pair1[i] == pair2[i]:
       result = 'bad'
       break
    else:
        pplno = pair1.index(pair2[i])
        if pair1[i] != pair2[pplno]:
            result = 'bad'
            break
print(result)

