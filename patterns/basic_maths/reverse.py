def rev(num):
    dup=num
    rev=0
    while num>0:
        lastdigit=num%10
        rev=(rev*10)+lastdigit
        num=num//10
    return rev
num=int(input("Enter a number:"))
print(f"Reverse of {num} is {rev(num)}") 
