# CCC 2013 Junior 3: From 1987 to 2013

# find the next year after a given year with distinct digits.

# this is a big cheat: but python can count letters in a string :-)
# Problem Description
# You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years
# 2014, 2015, 2016, 2017, 2018, 2019 each have distinct digits. 2012 does not have distinct digits,
# since the digit 2 is repeated.
# Given a year, what is the next year with distinct digits?
# Input Specification
# The input consists of one integer Y (0 ≤ Y ≤ 10000), representing the starting year.
# Output Specification
# The output will be the single integer D, which is the next year after Y with distinct digits.

#year = input() + 1
vInput = ['1987']
year = int(vInput[0]) + 1

duplicateFlag = True
while duplicateFlag:
    duplicateFlag = False
    yearString = str(year)
    for digit in yearString:
        if yearString.count(digit) > 1:
            duplicateFlag = True
    year = year + 1

print(year)