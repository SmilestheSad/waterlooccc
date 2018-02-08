
#Access list inside list
list2=[[1,2,3,4],[2,3,4,5],3,8]
print(list2[1][2])
#List Method
list1= list(range(1,9))  # generate list from range - [1, 2, 3, 4, 5, 6, 7, 8]
squares = [1, 4, 9, 16, 25, 36, 49, 64]  # generate a manual list
squares.sort(reverse=True)  # order decent
squares.append(9**2) # insert a list element at the end
squares.remove(9)  # remove numner 5 from list
del squares[2] # delete third element from list
squares[0] = 100 # update first element to 100
squares.pop()   #remove last element and return popped element
squares.insert(3,9999) # insert 999 at index 3 (after fourth element)

#List  Operation
len(squares)   #Length,
concatenationList = squares + [5,6,7,8] # Join two list
mutiplyList = ['a'] * 20  # Generate list with 20 a's
listAverge = sum(concatenationList)/len(concatenationList) # total/number of elements

mutiplyList1 = list1 * 3  # repeat list1 for 3 times

#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#List Comprehension
squares1 = [ x**2 for x in range(1,9)]  # [1, 4, 9, 16, 25, 36, 49, 64]
#Convert string list to int list
sList = "1 2 5 6 9 10"
sListInt = [int(x) for x in sList.split() ]  # convert sList to list and convert list element to int
sListInt1 = [int(x)**2 for x in sList.split() ]  # convert sList to list and convert list element to int and power

sList1 = "aa bb ccdd aadd ee"
sListNew = [len(s) for s in sList1.split() ]  # generate list with length of string for each element
sListNew2 = [s for s in sList1.split() if (s.count('aa') > 0 )]  # generate list with length of string for each element if string contain 'aa'



#split digits into ones/tens/hundreds
input_number = 1234
ones = (input_number%10)
tens = int(str(input_number)[-2])
hundreds = int(str(input_number)[-3])
thousands = int(str(input_number)[-4])


#http://www.cemc.uwaterloo.ca/contests/computing/2011/stage1/seniorEn.pdf J2
# 2016 J1
#http://www.cemc.uwaterloo.ca/contests/computing/2014/stage%201/juniorEn.pdf   J3