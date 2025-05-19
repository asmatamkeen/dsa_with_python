def count_digits(num):
    count=0
    while num>0:
        lastdigit=num%10
        count=count+1
        num=num//10
    return count
num=int(input("Enter a number:"))
num_digits=count_digits(num)
print(f"Number of digits in {num} is {num_digits}")