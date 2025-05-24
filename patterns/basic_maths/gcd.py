def gcd(num1,num2):
    lst=[]
    for i in range(1,num1+1):
        if i%num1==0:
            lst.append(i)
    lst1=[]
    for j in range(1,num2+1):
        if j%num2==0:
            lst1.append(j)
    common=[]
    for k in lst1:
        for l in lst:
            if lst1[k]==lst[l]:
                common.append(k)

    gcd=max(common)
    return gcd
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(f"GCD of {num1} and {num2} is {gcd(num1,num2)}")


        