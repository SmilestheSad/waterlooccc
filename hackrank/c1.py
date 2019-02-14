s = list(input())

#Put this as global variable
vowel = list("aeiou")
cons = [list("bcd"),list("fgh"),list("jklmn"),list("pqrst"),list("vwxyz")]


# You only need translate cons not vowl
def translate(b):
    res = ''
    if b in vowel:
        res = b
    else:
        res = translateCons(b)
    print(b,res)
    return res


# Function to translate cons
def translateCons(b):
    
    ncons,nvowel = '',''  # ncons/nvowel must be declared. Otherwise it will diappear after IF block is done
    spice = []  # same
    
    for y in range(len(cons)):
        # for x in range(len(cons[y])):  # No need to loop , use  "IN" to check
            # if cons[y][x] == s:   s is orignal string, b is A letter passed to function
        if  b in cons[y] :  # check if letter is in one of cons group
            
            x = cons[y].index(b)  #Get index of cons , y is index of vowel
            spice = [y,x] 
            try:
                ncons = cons[y][x+1]
                break
            except:
                try:
                    ncons = cons[y+1][0]
                    break
                except:
                    ncons = "z"
                    break
    # y is gone after IF 
    if spice[1] <= len(cons[spice[0]])//2:
    # if x <= len(cons[y])//2:  # optional if spice is not used
        # nvowel = vowel[spice[y]]
        nvowel = vowel[spice[0]]  #confused with y... 
    else:
        # nvowel = vowel[spice[y+1]]
        try:
            nvowel = vowel[spice[0] + 1]  #confused by y
        except:
            nvowel = 'u'  # If cons is "y", since you have to use last vowel "u"

    # res = "".join([s,nvowel,ncons])   
    res = "".join([b,nvowel,ncons])     # b not s
    return res  # Good habit to return simple variable  so you can debug


new  = [translate(x) for x in s]
print("".join(new))