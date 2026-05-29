def pivotIndex(nums):
    left_sum = 0
    right_sum = 0
    total_sum = sum(nums)
    for i in range(0,len(nums)-1):
        left_sum = left_sum + nums[i]
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
    return -1

print(pivotIndex([1,7,3,6,5,6]))