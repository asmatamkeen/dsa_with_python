def maxWater(height):
    maxarea=0
    j=len(height)-1
    i=0
    while i<j:
        lv=height[i]
        rv=height[j]
        minv=min(lv,rv)
        widthh=abs(i-j)
            
        if maxarea<=(minv*widthh):
            maxarea=(minv*widthh)
        if height[i]<=height[j]:
            i +=1
        else:
            j -= 1

    print(maxarea)

maxWater([1,8,6,2,5,4,8,3,7])