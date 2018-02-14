l = [ '1','2','3', '4','10','1']
#Create list clone
l2=l
l.pop()  # l = [ '1','2','3', '4','10'] , l2 is changed too.
l2=l[:]

newlist = []
# Convert all element to int  [1,2,3,4,10,1]
for i in range(len(l)):
   newlist = newlist.append(int(l[i]))
l4 = [ int(x) for x in l ]
# Insert 100 to end of list
l.append(100)
# Replace first element with 3
l[0] = 3
# Find index of element 10
l.index(10)
# Remove duplicate element
list(set(l))
# generate list with even number only output: [2,4,10]
l5 = [x for x in l if x%2 == 0]
# Largest number output: 10  - find 3 different ways 
max(l)
# sum,average(mean),mode,median
sum(l)
sum(l)/len(l)


list1= [3,5,6,8]
list2 =[3,4,7,10]

# Join two list   output: [3,5,6,8,3,5,6,8]

# sum each element [ 3+3,5+5,6+7,8+10]
