a=int(input("Enter number of rows:"))
for i in range(a,0,-1):
    print(" "*(a-i),end="")
    print("*"*(2*i-1))
