# • if the given text has more “t” and “T” characters than “s” and “S” characters, we will say
# that it is (probably) English text;
# • if the given text has more “s” and ”S” characters than “t” and “T” characters, we will say
# that it is (probably) French text;
# • if the number of “t” and “T” characters is the same as the number of “s” and “S” characters,
# we will say that it is (probably) French text.

#vInput=['3','The red cat sat on the mat.','Why are you so sad cat?','Don’t ask that.']
vInput=['3','Lorsque j’avais six ans j’ai vu, une fois,','une magnifique image,','dans un livre']

textList=vInput[1:]

countT=sum([ s.count('T') for s in textList]) + sum([ s.count('t') for s in textList])
countS=sum([ s.count('S') for s in textList]) + sum([ s.count('s') for s in textList])

if ( countS < countT):
    print('English')
else :
    print('French')