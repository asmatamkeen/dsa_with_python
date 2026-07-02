def pattern10(n):
    for i in range(1,n):
        print('*'*i)
    for i in range(n,0,-1):
        print('*'*i)   
pattern10(5)