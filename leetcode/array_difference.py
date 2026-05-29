def findDifference(nums1, nums2):
    nums = []
    nums.append(list(set(nums1)- set(nums2)))
    nums.append(list(set(nums2)- set(nums1)))
    return nums
print(findDifference([1,2,3], [2,4,6]))