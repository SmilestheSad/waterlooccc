from sys import stdin

# vInput = [ x.strip() for x in stdin]
with open('../data/J5/j5.1-2.in') as f:
    vInput = [line.strip() for line in f]

pages = int(vInput[0])
pageQuestionList = vInput[1:]
print(pageQuestionList)

checkedPageList = list(range(1,pages+1))
hopsList= list()
def markVisitedPage(page,visitedPageList,hops):
    
    if ( page in visitedPageList):
        print("remove",page,checkedPageList)
        checkedPageList.remove(page)
        currentQuestion = pageQuestionList[page-1].split()
        # print("current question",currentQuestion)
        if len(currentQuestion) >1:
            for pageStr in currentQuestion[1:] :
                markVisitedPage(int(pageStr),visitedPageList,hops+1)
                
        else:
            pass
    else:
        hopsList.append(hops)
        print('FinalMark',visitedPageList)

markVisitedPage(1,checkedPageList,1)
hopsList.sort()
print("least hops",hopsList[0])
#get list of directed page lines
