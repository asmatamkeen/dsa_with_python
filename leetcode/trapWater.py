def trap(height):
    left=0
    right=len(height)-1
    left_max=height[left]
    right_max=height[right]
    max_water=0
    while left<=right:
        if height[left]>left_max:
            left_max=height[left]
        if height[right]>right_max:
            right_max=height[right]
        if height[left]<height[right]:
            max_water=max_water+left_max-height[left]
            left += 1
        else:
            max_water=max_water+right_max-height[right]
            right -= 1
    return max_water



print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

        
