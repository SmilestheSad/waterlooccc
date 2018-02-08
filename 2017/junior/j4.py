def checkClock(mins):
    hour = mins//60
    if (hour == 0):
        hour = 12
    mins = mins % 60
    # convert to string
    clockString = "%0d%02d" % (hour, mins)
    result = 1
    diff = int(clockString[1]) - int(clockString[0])
    for i in range(2, len(clockString)):
        newdiff = int(clockString[i]) - int(clockString[i-1])
        if (newdiff != diff):
            result = 0
    return result


vInput = ['180']
mins = int(vInput[0])
count = 0
for i in range(mins+1):
    count = count + checkClock(i)

print(count)
