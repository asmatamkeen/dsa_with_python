def pattern17(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end='')
        for j in range(i+1):
            str_chr=chr(65+j)
            print(str_chr,end='')
        for j in range(i-1,-1,-1):
            ch=chr(65+j)
            print(ch,end='')
        print()
        


pattern17(5)