

#input the data
W = int(input())
N = int(input())

carWeight = [0,0,0]  #generate 3 dummy 0 weight train in front

for i in range(N):
    carWeight.append(int(input()))



def checkTrainPass(carWeight):
    carsAcross = 0
    final = N
    for i in range(N):
        
            # print(carWeight[i:i+4])
            weight = sum(carWeight[i:i+4])
            if weight <= W:
                carsAcross +=1
            else:
                final = carsAcross
                break
    return final

print(checkTrainPass(carWeight))

