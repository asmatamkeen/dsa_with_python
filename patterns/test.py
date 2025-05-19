def divisors(num):
    lst=[]
    for i in range(1,num+1):
        if num%i==0:
            lst.append(i)
            i=i+1
    return lst
num=int(input("Enter a number:"))
print(f"Divisors of {num} are {divisors(num)}")