def singleNumber(nums):
    res = 0
    for n in nums:
        res ^= n
    return res


print(singleNumber([2,2,1]))