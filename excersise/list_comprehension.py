list1 = [3,6,7,8]

newlist = [ x for x in list1]  # Duplicate list1
newlist = [ x+2 for x in list1]  # math 
newlist = [ str(x) for x in list1] # type convert

def dosomething(x):
    return x*2

newlist = [ dosomething(x) for x in list1] #
newlist = list(map(dosomething,list1))  # same as above. map function iterate fun to each element 


s = "0 1 2 3"
newlist = [ int(x) for x in s.split()] # type convert
newlist = [ int(x) for x in s.split() if (int(x) > 2)] # filter


s= "Not one to easily switch out of nurturing mode"
newlist =  [ x for x in s.split()]  #
newlist =  [ len(x) for x in s.split()]

s="abcdec"
newlist = [ x*2 for x in s]
newlist = [ x.upper() for x in s if x in ['a','b','c']]

#Generate a list

newlist = [ x**2 for x in range(1,5)] # [1,4,9,16]

