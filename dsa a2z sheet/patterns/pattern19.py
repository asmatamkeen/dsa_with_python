def pattern19(n):
    spaces1=0
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end='')
        for j in range(spaces1):
            print(' ',end='')
        spaces1+=2
        for j in range(i):
            print('*',end='')
        print()
    spaces=2*(n-1)
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        for j in range(1,spaces+1):
            print(' ',end='')
        spaces-=2
        for j in range(i+1):
            print('*',end='')
        print()
        
        
        

pattern19(5)