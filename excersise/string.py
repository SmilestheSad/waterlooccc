s = 'abcde'
# Delete first character output: bcde
s2=s[1:]
# Delete last charactor  output: abcd
# news=list(s)
# news.pop()
# s4 = ''.join(news)

s3=s[0:-1]
# swap second and third letter output: acbde
alist=list(s)
thirdLetter=alist[2]
secondLetter=alist[1]
alist[2]=secondLetter
alist[1]=thirdLetter
alist = "".join(alist)
# Reserve the string output:  edcba

# Count how many letters output : 5

# Insert space between each letter output: a b c d e

# double each letter  output: aabbccddee

# Print "First letter: a and last letter is Letter"



s="02:10"  # Hour and mins
#Convert to mins  130

i = 130 # convert to hour and print in lead 0 if hour and mins is less than 10


i=13
#Get next prime number 

#get 10th digit

i=5282
#Product largest possible number using those digits output: 8522
dab = list(str(i))
dab = [int(x) for x in dab]
dab.sort(reverse=True)
dab = [str(x) for x in dab]
number = ''.join(dab)
print(number)
