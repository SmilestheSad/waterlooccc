# https://dmoj.ca/problem/ccc04s2

vInput=['5 2','99 97 100 85 -4','95 97 100 62 1000']
yodellerNumber=int(vInput[0].split()[0])
roundNumber=int(vInput[0].split()[1])
scoreList=vInput[1:]  # ['99 97 100 85 -4', '95 97 100 62 1000']

#Convert string to list
scoreListinList= [ x.split() for x in scoreList]
# [['99', '97', '100', '85', '-4'], ['95', '97', '100', '62', '1000']]

scoreTotal=[]
# Find highest score
for x in range(yodellerNumber):
    total = 0
    for y in range(roundNumber):
        total = total + int(scoreListinList[y][x])
        #First time x=0,y=0,total=0 after total = 0 + 99 = 99
        #Second time x=0,y=1, total=99 after total= 99 + 95 =194
    scoreTotal.append(total)    

# ScoreTotal after all loop    
# [194, 194, 200, 147, 996]

#Find Higest score and yodeller #
maxScore = max(scoreTotal)
maxYdeller= scoreTotal.index(maxScore)

#Find worst rank
yList = [ x[maxYdeller] for x in scoreListinList]

for y in range(roundNumber):
    tlist = scoreListinList[y]
    tlist.sort()


print('Yodeller 5 is the TopYodeller: score 996, worst rank 5')
