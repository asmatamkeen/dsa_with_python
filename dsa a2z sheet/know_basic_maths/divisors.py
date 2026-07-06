def divisors(n):
    divi = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divi.append(i)
            if i!=(n//i):
                divi.append(n//i)
    divi.sort()
    return divi
                    
print(divisors(6))