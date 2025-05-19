def armstrong(num):
    dup=num
    arms=0
    while num>0:
        ld=num%10
        arms=arms+(ld*ld*ld)
        num=num//10
    if arms==dup:
        return "true"
    else:
        return "false"
num=int(input("Enter a number:"))
print(f"{armstrong(num)}")
