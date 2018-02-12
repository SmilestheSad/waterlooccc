ss = "sammy shark"
# String Convert  SAMMY SHARK \n Sammy shark
print(ss.upper(), ss.capitalize())
# mys krahs ymmas shark 11 2
print(ss[2:8:2])  # print every other letter starting from third one
print(ss[::-1])  # reverse string
print(len(ss), ss.count('a'))
sList = "1 2 5 6 9 10"
# Convert string to list and get subset ['5', '6','9']
sListNew = sList.split()[2:4]


# OUTPUT: False False True True False
print(ss.isnumeric(), ss.isupper(), ss.islower(),
      ss.startswith("sa"), ss.endswith("victor"))

# join,split,replace
sHappy = "I’m happy-:).I’m sad-:(  I’m happy again-:)"  # 2015/J2
happyCount = sHappy.count('-:)')
sadCount = sHappy.count('-:(')

# Remove Certain string
s3 = "abcaaabcdddaaa"
print(''.join(s3.split('a')))  # bcbcddd
print(s3.replace('a', ''))  # bcbcddd

"".join(reversed(ss))  # Reserve string ss  Same as "ss[::-1]"
# sharks,crustaceans,plankton
print(",".join(["sharks", "crustaceans", "plankton"]))

# String Format Print
year, month, day, hour, mins = 2017, 1, 23, 1, 4
# %02d means padding string "0", print width 2, "d" means a int(digit) variable will be placed
print("%d-%02d-%02d  %02d:%02d" % (year, month, day, hour, mins))
aFloat = 3.1
print("%.05f" % (aFloat)) # 3.10000 - padding 0, print 5 digits after dot

# String Operation plus and multiply -   2003/J1
vString1, vString2 = "*", ' '
n = 3
for i in range(4):
    print(vString1 + vString2*n + vString1 + vString2*n + vString1)
