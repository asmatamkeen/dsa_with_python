a=int(input("Enter number of half-rows:"))
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("*"*(2*i-1))
for i in range(a,0,-1):
    print(" "*(a-i),end="")
    print("*"*(2*i-1))

