def swapcode(newList):
    size = len(newList)
    temp=newList[0]
    newList[0]= newList[size-1]
    newList[size-1]=temp
    return newList
newList = [5,25,50,100,105 ]
print(swapcode(newList))



#  Different approach
def swapcode_v1(newListv1):
    newListv1[0] ,  newListv1[-1] = newListv1[-1], newListv1[0]
    return newListv1
newListv1= [5,25,50,100,105 ]
print(swapcode_v1(newListv1))



# Different approach
def swapcode_v2(newListv2):
    get= newListv2[-1], newListv2[0]
    newListv2[0],newListv2[-1]=get 
    return newListv2
newListv2= [5,25,50,100,105 ]
print(swapcode_v2(newListv2))
