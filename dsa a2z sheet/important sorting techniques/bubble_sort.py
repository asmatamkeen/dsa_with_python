def bubbleSort(nums):
    for i in range(len(nums)-1,-1,-1):
        swapped=False
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped=True
        if not swapped:
            break
    return nums
print(bubbleSort([7,4,1,5,3]))