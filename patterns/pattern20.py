a=int(input("Enter number of rows:"))
for i in range(1,a+1):
    for j in range(i):
        print("*",end="")
    for spaces in range(a-i):
        print(" ",end="")
    for spaces in range(a-i):
        print(" ",end="")
    for j in range(i+1,1,-1):
        print("*",end="")
    print()
for i in range(a-1,0,-1):
    for j in range(i):
        print("*",end="")
    for spaces in range(a-i):
        print(" ",end="")
    for spaces in range(a-i):
        print(" ",end="")
    for j in range(i+1,1,-1):
        print("*",end="")
    print()
