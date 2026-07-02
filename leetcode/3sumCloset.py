def threesumclosest(nums,target):
    nums.sort()
    for i in range(0,len(nums)-1):
        left = i+1
        right=len(nums)-1
        current_sum=nums[i]+nums[left]+nums[right]
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1

        else:
            pass
    return current_sum

print(threesumclosest([-1,2,1,-4],1))