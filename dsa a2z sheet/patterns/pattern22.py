def pattern22(n):
    size=2*n-1
    for i in range(size):
        for j in range(size):
            top=i
            left=j
            bottom=size-1-i
            right=size-1-j
            print(n-min(left,right,top,bottom),end=' ')
        print()
    
pattern22(5)