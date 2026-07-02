def pattern7(n):
    for i in range(0,n):
        print(' '*(n-i),end='')
        print('*'*((i*2)+1))
pattern7(5)