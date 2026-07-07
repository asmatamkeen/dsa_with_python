def mostFrequentElement(nums):
    hash={}
    for i in range(0,len(nums)):
        if nums[i] not in hash:
            hash[nums[i]]=0
        hash[nums[i]]+=1
    max_value=0
    ans=None
    for number, frequency in hash.items():
        if frequency>max_value:
            ans=number
            max_value=frequency
        elif frequency == max_value:
            if number<ans:
                ans=number
        
    return ans
print(mostFrequentElement([1,2,2,2,2,3,3,3,3]))