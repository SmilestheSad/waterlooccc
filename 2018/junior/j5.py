from sys import stdin

# vInput = [ x.strip() for x in stdin]
with open('../data/J5/j5.1-1.in') as f:
# with open('../data/J5/j5.1-2.in') as f:
# with open('../data/J5/j5.2-1.in') as f:
# with open('../data/J5/j5.1-3.in') as f:
    vInput = [line.strip() for line in f]

pages = int(vInput[0])
pageQuestionList = vInput[1:]
# print(pageQuestionList)

hopList = []
def markVisitedPage(page,checkedPageList,hops):
    
    currentQuestion = pageQuestionList[page-1].split()
    if len(currentQuestion) >1:
        for nextPage in currentQuestion[1:] :
            # pageOrderList.append(int(pageStr))

            #check if next page has been used
            if ( page in checkedPageList):
                # print("remove",page,checkedPageList)
                checkedPageList.remove(page)
                print('function is called',page,nextPage,hops)
                markVisitedPage(int(nextPage),checkedPageList,hops+1)
            # hops = parentHops
            
    else:
        # print('End Page is reached',page,hops)
        print('END/PAGE HOPS',hops)
        hopList.append(hops)



checkedPageList = list(range(1,pages+1))
# pathList= list()
# minHops = pages
markVisitedPage(1,checkedPageList,1)
# minPages = [len(x) for x in pathList].sort()
#get list of directed page lines
# print(hopList)
print(checkedPageList)
hopList.sort()
print(hopList[0])
