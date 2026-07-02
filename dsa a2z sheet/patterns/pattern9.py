def pattern9(n):
    for i in range(0,n+1):
        print(' '*(n-i),end='')
        print('*'*((2*i)-1))
    for i in range(n,0,-1):
        print(' '*(n-i),end='')
        print('*'*((2*i)-1))
pattern9(5)