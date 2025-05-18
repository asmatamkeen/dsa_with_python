a=int(input("Enter number of rows:"))
n=1
for i in range(1,a+1):
    for j in range(i):
        print(n,end=" ")
        n=n+1
    print()