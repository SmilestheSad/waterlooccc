# CCC 2013 Junior 2: Rotating Letters

# Problem Description

# An artist wants to construct a sign whose letters will rotate freely in the breeze. In order to do this,
# she must only use letters that are not changed by rotation of 180 degrees: I, O, S, H, Z, X, and N.
# Write a program that reads a word and determines whether the word can be used on the sign.
# Input Specification
# The input will consist of one word, all in uppercase letters, with no spaces. The maximum length
# of the word will be 30 letters, and the word will have at least one letter in it.
# Output Specification
# Output YES if the input word can be used on the sign; otherwise, output NO.

vInput=['SHINS']   # answer is YES
#vInput=['NOISE']    # answer is NO
word=vInput[0]

rotate = "IOSHZXN"
answer = "YES"
for letter in word:
    if letter not in rotate:
        answer = "NO"
        
print(answer)
