a=int(input("Enter number of rows:"))
for i in range(a,0,-1):
    for ch in range(ord("A"),ord("A")+i):
        print(chr(ch),end='')
    print()