def selection_sort(nums):
    for i in range(0,len(nums)):
        mini=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[mini]:
                mini=j
        nums[mini],nums[i]=nums[i],nums[mini]
    return nums
print(selection_sort([7 ,4 ,1 ,5 ,3]))