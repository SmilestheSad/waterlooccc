#Basic for loop in [0,1,2,3]
#Sample1 : For Loop
list1 = range(4)
total = 0
for i in list1:  # OR for in in range(4)
    total = total + 2**i

#Sample2 :Whille Loop with True condition and break statement
counter=0
total = 0
while True:
    if (counter <=3):
        total = total + counter
        counter = counter + 2**i
    else:
        break    

#Whille Loop with counter condition 
counter=0
total = 0
while (counter <=3):
    total = total + counter
    counter = counter + 1

#One Line Code
total = sum([2**i for i in range(4)])

#Basic for loop in a string list
#  for loop variable is list element
list2=['qwq','rere','bbbbb','cccccc']
totalLength=0
for s in list2:   
    totalLength = totalLength + len(s)
    print(s,len(s),totalLength)

#loop variable is list index based on range(4)
for i in range(len(list2)):  
    totalLength = totalLength + len(list2[i])
    listString= list2[i]
    print(listString,len(listString),totalLength)    

#One line code
totalLength = sum([len(s) for s in list2])
print(totalLength)