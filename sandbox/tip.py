orders=5
aMaxOrder = 3
bMaxOrder = 3
aTipList = [5,4,3,2,100]
bTipList = [1,2,3,4,5]


def getMaxTip(orders,aMaxOrder,bMaxOrder,aTipList,bTipList):
    totalTips,aOrders,bOrders = 0,0,0
    maxTipList = [ aTipList[i] if aTipList[i] > bTipList[i] else bTipList[i] for i in range(orders)   ]
    print(maxTipList)
    # for o in range(orders):
    #     if (aTipList[o] > aTipList[o]):
    #         totalTips = totalTips + aTipList[o]
    #         aOrders = aOrders + 1
    #     else:
    #         totalTips = totalTips + bTipList[o]
    #         bOrders = bOrders + 1



getMaxTip(orders,aMaxOrder,bMaxOrder,aTipList,bTipList)