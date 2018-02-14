from sys import stdin 
vInput = [x.strip() for x in stdin]
# vInput = [20,10,150]
angle1 = int(vInput[0])
angle2 = int(vInput[1])
angle3 = int(vInput[2])
if (angle1 + angle2 + angle3) == 180:
    if angle1 == angle2 == angle3:
        print("Equilateral")
    elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")