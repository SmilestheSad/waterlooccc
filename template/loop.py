base, shift = 12, 3

# Sample1 : For Loop
total = 0
for i in range(shift+1):  # OR for in in range(4)
    total = total + base*10**i
print("Sample1 Result:", total)

# Sample2 - Whille Loop with True condition and break statement
total, counter = 0, 0
while True:
    if (counter <= shift):
        total = total + base*10**counter
        counter = counter + 1
    else:
        break
print("Sample2:", total)

# Sample 3 -  Whille Loop with counter condition
total, counter = 0, 0
while (counter <= shift):
    total = total + base*10**counter
    counter = counter + 1
print("Sample3:", total)

# One Line Code
total = sum([12*10**i for i in range(shift+1)])
print("One Line Code for shift number:", total)

# Basic for loop in a string list
# loop variable is list element
list2 = ['qwq', 'rere', 'bbbbb', 'cccccc']
totalLength = 0
for s in list2:
    totalLength = totalLength + len(s)
    #print(s, len(s), totalLength)

# loop variable is list index
for i in range(len(list2)):
    totalLength = totalLength + len(list2[i])
    listString = list2[i]
    #print(listString, len(listString), totalLength)

# One line code
totalLength = sum([len(s) for s in list2])
print("Total letter in List is:",totalLength)
