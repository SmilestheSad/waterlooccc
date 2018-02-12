list1 = [3,6,7,8]

newlist = [ x for x in list1]  # Duplicate list1
newlist = [ x+2 for x in list1]  # math 
newlist = [ str(x) for x in list1] # type convert

def dosomething(x):
    return x*2

newlist = [ dosomething(x) for x in list1] #


s = "0 1 2 3"
newlist = [ int(x) for x in s.split()] # type convert
newlist = [ int(x) for x in s.split() if (int(x) > 2)] # filter


s= "Not one to easily switch out of nurturing mode"
newlist =  [ x for x in s.split()]  #
newlist =  [ len(x) for x in s.split()]

s="abcdec"
newList = [ x*2 for x in s]
newlist = [ x.upper() for x in s if x in ['a','b','c']]

print('test')