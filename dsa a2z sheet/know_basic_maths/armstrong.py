def armstrong(n):
    original=n
    length=len(str(n))
    num=0
    while n>0:
        last_digit=n%10
        num+=pow(last_digit,length)
        n=n//10
    return 'true' if original==num else 'false'
print(armstrong(153))