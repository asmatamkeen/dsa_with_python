def gcd(num1,num2):
    lst1=[]
    for i in range(1,num1+1):
        if num1%i==0:
            lst1.append(i)
    print(lst1)
    lst2=[]
    for j in range(1,num2+1):
        if num2%j==0:
            lst2.append(j)
    print(lst2)
    common=[]
    for i in lst1:
        if i in lst2:
                common.append(i)
    print(common)

    gcd=max(common)
    return gcd
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(f"GCD of {num1} and {num2} is {gcd(num1,num2)}")



        