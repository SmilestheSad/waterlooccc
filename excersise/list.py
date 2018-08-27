list1= [ '1','2','3', '4','10','1'] #mutable list
#Create list clone
list2=list1
list1.pop()  # l = [ '1','2','3', '4','10'] , l2 is changed too.
print(list2)

list2=list1[:]

newlist = []
# Convert all element to int  [1,2,3,4,10,1]
# for i in range(len(l)):
#    newlist = newlist.append(int(l[i]))
listInt = [ int(x) for x in list1 ]
# Insert 100 to end of list
list1.append(100)
# Replace first element with 3
list1[0] = 3
# Find index of element 10
# list1.index(1)
# Remove duplicate element
list(set(list1))
# generate list with even number only output: [2,4,10]
list1 = [x for x in listInt if x%2 == 0]
# Largest number output: 10  - find 3 different ways 
max(list1)
# sum,average(mean),mode,median
sum(list1)/len(list1)


list1= [3,5,6,8]
list2 =[3,4,7,10]
# list1.append(list2)

# list2 = list1.extend(list2)


vSet1=set(list1)
vSet2=set(list2)

print(vSet1.intersection(vSet2))
print(vSet1.difference(vSet2))
print(vSet1.union(vSet2))

# Join two list   output: [3,5,6,8,3,5,6,8]

# sum each element [ 3+3,5+5,6+7,8+10]
