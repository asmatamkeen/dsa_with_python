def containsDuplicate(nums, k):
    list1={}
    for i, num in enumerate(nums):
        if num in list1:
            if i-list1[num]<=k:
                return True
        list1[num]=i
    
    return False
    

print(containsDuplicate([1,2,3,1,2,3],2))