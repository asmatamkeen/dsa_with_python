def largestElement(nums):
    max=nums[0]
    for i in range(1,len(nums)):
        if nums[i]>max:
            max=nums[i]
    return max

print(largestElement([1,2,3,4,5,77]))