def countFrequencies(nums):
    hash={}
    for i in range(0,len(nums)):
        if nums[i] not in hash:
            hash[nums[i]]=0
        hash[nums[i]]+=1
    nums1=[]
    for num in hash:
        nums1.append([num,hash[num]])
    return nums1
print(countFrequencies([3,3,3,3]))