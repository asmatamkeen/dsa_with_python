def palindrome(num):
    dup=num
    rev=0
    while num>0:
        lastdigit=num%10
        rev=(rev*10)+lastdigit
        num=num//10
    if dup==rev:
        return "true"
    else:
        return "false"
num=int(input("Enter a number:"))
print(f"{palindrome(num)}")  
