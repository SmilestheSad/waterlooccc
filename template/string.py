ss = "sammy shark"

print(ss.upper() + "\n",ss.capitalize()) #String Convert  SAMMY SHARK \n Sammy shark
#mys krahs ymmas shark 11 2
print(ss[2:8:2], ss[::-1],ss[-5:], len(ss),ss.count('a')) 

#OUTPUT: False False True True False
print(ss.isnumeric(),ss.isupper(),ss.islower(), ss.startswith("sa"),ss.endswith("victor")) 


# join,split,replace
sList = "1 2 5 6 9 10"
sHappy = "I’m happy-:).I’m sad-:(  I’m happy again-:)"
sListNew = sList.split()[2:6]   # Convert string to list  ['5', '6']
#Convert string list to int list
sListNewInt = [int(x) for x in sListNew ]
print(sListNewInt)


#Count sub-string occurance
iHappy = sHappy.split("-:)")  # ['I’m happy', '.I’m sad-:(  I’m happy again', '']
iSad= sHappy.split("-:(") # ['I’m happy-:).I’m sad', '  I’m happy again-:)']
print(len(iHappy) -1 ,len(iSad) -1)  # OUTPUT: 2 1

#Remove Certain string
s3="abcaaabcdddaaa"
print(''.join(s3.split('a')))  #bcbcddd
print(s3.replace('a',''))  #bcbcddd


"".join(reversed(ss))  # Reserve string ss
print(",".join(["sharks", "crustaceans", "plankton"]))  #sharks,crustaceans,plankton