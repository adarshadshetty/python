def swapcode(newList):
    size = len(newList)
    temp=newList[0]
    newList[0]= newList[size-1]
    newList[size-1]=temp
    return newList
newList = [5,25,50,100,105 ]
print(swapcode(newList))
