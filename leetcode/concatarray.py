def concatWithReverse(list):
    list1=list.copy()
    j=-1
    for i in range (0, int(len(list)/2)):
        list[i],list[j]=list[j],list[i]
        j-=1
    list1=list1+list
    return list1
print(concatWithReverse([1,2,3,4]))
        
