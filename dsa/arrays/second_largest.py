def secondLargest(arr):
    first_largest=-1
    second_largest=-1
    for i in range(0,len(arr)):
        if arr[i]>first_largest:
            second_largest=first_largest
            first_largest=arr[i]
        
    return second_largest

print(secondLargest([1,2,3,4,5,6]))