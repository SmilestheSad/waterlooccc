
list1 = list(range(1, 9)) # generate list from range - [1, 2, 3, 4, 5, 6, 7, 8
# Access list inside list
list2 = [[1, 2, 3, 4], [2, 3, 4, 5], 3, 8]
print(list2[1][2])   # 4

# List Method
squares = [1, 4, 9, 16, 25, 36, 49, 64]  # generate a manual list
squares.sort(reverse=True)  # order decent
# [64, 49, 36, 25, 16, 9, 4, 1]
squares.append(9**2)  # insert a list element at the end
#[64, 49, 36, 25, 16, 9, 4, 1, 81]
squares.remove(81)  # remove number 81 from list
#[64, 49, 36, 25, 16, 9, 4, 1]
del squares[2]  # delete third element(36) from list
#[64, 49, 25, 16, 9, 4, 1]
squares[0] = 100  # update first element to 100
#[100, 49, 25, 16, 9, 4]
squares.pop()  # remove last element and return popped element
#[100, 49, 25, 16, 9, 4]
squares.insert(3, 9999)  # insert 999 at index 3 (after fourth element)
#[100, 49, 25, 9999, 16, 9, 4]
list(set(squares)) #gerate a distinct list(remove duplicate)

# List  Operation
listTest1= [1,1,3,4,34,3]
listLength = len(listTest1)  # 6  - Length for both list and string 
uniqueList = list(set(listTest1))  # remove duplicate for both list and string
#[1, 34, 3, 4]
concatenationList = listTest1 + [5, 6, 7, 8]  # Join two list
# 1, 1, 3, 4, 34, 3, 5, 6, 7, 8]
multiplyList = ['a'] * 3 # Generate list with 20 a's - both list and string
#['a','a','a']
multiplyList1 = listTest1 * 2  # repeat list1 for 3 times
#[1, 1, 3, 4, 34, 3, 1, 1, 3, 4, 34, 3]
listRange = max(listTest1) - min(listTest1)  # only list is int
listAverge = sum(concatenationList) / len(concatenationList)  # total/number of elements

# List Comprehension
squares1 = [x**2 for x in range(1, 9)]  # [1, 4, 9, 16, 25, 36, 49, 64]
#Above code is written in regular loop to understand the logic
squares1 = []
for x in range(1,9):
    newValue = x**2
    squares1.append(newValue)

# Convert string list to int list
aString = "1 2 5 6 9 10"
# convert sList to list and convert list element to int
sListInt = [int(x) for x in aString.split()]
# convert sList to list and convert list element to int and power
sListInt1 = [int(x)**2 for x in aString.split()] # 
sList1 = "aa bb ccdd aadd ee"
# generate list with length of string for each element
sListNew = [len(s) for s in sList1.split()]   # [2, 2, 4, 4, 2]
# generate list with length of string for each element if string contain 'aa'
sListNew2 = [s for s in sList1.split() if (s.count('aa') > 0)]


# split digits into ones/tens/hundreds
input_number = 1234
ones = (input_number % 10)  # 4  
tens = int(str(input_number)[-2])  # 3
hundreds = int(str(input_number)[-3])  # 2
thousands = int(str(input_number)[-4])  # 1
