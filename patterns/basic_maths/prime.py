def prime(num1):
    count=0
    for i in range(1,num1+1):
        if num1%i==0:
            count=count+1
    if count==2:
        return "true"
    return "false"
num1=int(input("Enter num1:"))
print(prime(num1))