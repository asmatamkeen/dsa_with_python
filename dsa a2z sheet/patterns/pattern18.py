def pattern18(n):
    for i in range(n):
        str_chr=65+n-1-i
        for j in range(i+1):
            ch=chr(str_chr+j)
            print(ch,end='')
        print()
pattern18(5)