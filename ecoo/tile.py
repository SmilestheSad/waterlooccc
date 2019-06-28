wordMap = {
    'xooooo':'a',
    'xoxooo':'b',
    'xxoooo':'c',
    'xxoxoo':'d',
    'xooxoo':'e',
    'xxxooo':'f',
    'xxxxoo':'g',
    'xoxxoo':'h',
    'oxxxxo':'t',
    'oxxxox':'w',
    'oooooo':' ',
}

def translate(s):
    a = wordMap.get(s,'X')
    return a
    

test = '''oxxoxooxoooxoxoooxxoxoooxooxxoooxoxxooxoooxoxoxoxo
xxxxooxxooxoxoooxxxxoxooooxooxoooxxoooooooxooxoxoo
oxooooxoooooxoooxoooooooxxxoooooxoooooooooooxoxoxo
oxoxoxxoxoxooxooxxoxxxoxxoxoxooxooxoxoooxxxoxxxoxoxooxxooxoxxoxxox
xxxoxxxxoxooxxooxoxoooxxooxxoxxooooxxxoooooxoxxooxxxxoooxxxooxoxxo
oxooxoooxoxxxoooxoooooxoxxxoooxoooxoxoooooxoxoxxooxoxoooxoooxoxoxo
xoxoooxxxxooxoxoxooxooxoxxxxoooxxooxoxxoxoxooxoo
oxxxoooooxoooxooxxxooooooxoxooxxxxxoxooooxxxxooo
xoooooxoxxooooooxoxoooooxooooooxooooxoxoooxoxooo
xoxooxooxoxooxxooooxoxoxooxxxooxoxoxxxxx
xxoxxxooxoooxxoxooxoxxxoooxxoxxxxxxooxxx
ooxooxooxoooxoooooooxoxoooooooxoxoooxooo
xxxoxooxxoxooxxoxoooxoxxxxooxxxoxooxxoxooxxoxo
ooooxxxooxooxooxxxoooooxoxooooooxxxooxooxooxxx
ooxxxoooxoxxxoooxoooooxoooooooxxxoooxoxxxoooxo'''

test  =test.split('\n')



for i in range(len(test)//3):
    l1 = test[i*3]
    l2 = test[i*3+1]
    l3 = test[i*3+2]
    lineWidth = len(l1)
    lineW = []
    for j in range(lineWidth//2):
        w = l1[j*2:j*2+2] +l2[j*2:j*2+2] +l3[j*2:j*2+2]
        lineW.append(translate(w))
    print(''.join(lineW))
