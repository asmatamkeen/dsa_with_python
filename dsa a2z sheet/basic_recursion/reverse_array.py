def reverseArr(n,arr):    
    def reverse_recur(i):
        if i>=n/2:
            return
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        reverse_recur(i+1)
    reverse_recur(0)

    return arr
print(reverseArr(5,[1,2,3,4,5]))