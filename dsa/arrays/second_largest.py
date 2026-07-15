def secondLargest(arr):
    if (len(arr)<2):
        return None
    first_largest=-1
    second_largest=-1
    for i in range(0,len(arr)):
        if arr[i]>first_largest:
            second_largest=first_largest
            first_largest=arr[i]
        elif arr[i]>second_largest and arr[i]!=first_largest:
            second_largest=arr[i]

        
    return second_largest

print(secondLargest([4,9,9,0,2,8,7,1]))