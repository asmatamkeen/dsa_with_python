def largestElement(nums):
    max=nums[0]
    for i in range(1,len(nums)):
        if nums[i]>max:
            max=nums[i]
    return max

print(largestElement([4,9,0,2,8,7,1]))