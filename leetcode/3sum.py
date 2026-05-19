def threeSum(nums):
    res= []
    nums.sort()
    for i in range(0,len(nums)-2):
        if nums[i] == nums[i-1]:
            continue

        left = i+ 1
        right = len(nums) - 1
        while left < right :
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                list1= [nums[i], nums[left],nums[right]]
                res.append(list1)
                left += 1
                right -= 1
                
                while left<right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1


                
            elif total < 0:
                left += 1
            else:
                right -= 1

    return res


    
print(threeSum([-1,0,1,2,-1,-4]))