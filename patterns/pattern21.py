a=int(input("Enter number of rows:"))
for i in range(a):
    for j in range(a):
        if i==0 and i==a:
            print("*"*a)

    print("*",end='')
    print(" "*(a-2),end='')
    print("*",end='')
    print()
