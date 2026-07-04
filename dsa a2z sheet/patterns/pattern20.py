def pattern20(n):
    spaces=2*(n-1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('*',end='')
        for j in range(1,spaces+1):
            print(" ",end='')
        for j in range(i,0,-1):
            print('*',end='')
        print()
        spaces-=2
    spaces1=2
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print('*',end='')
        for j in range(spaces1,0,-1):
            print(" ",end='')
        for j in range(i,0,-1):
            print('*',end='')
        print()
        spaces1+=2
    
pattern20(4)