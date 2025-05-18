a=int(input("Enter number of rows:"))
for i in range(1,a+1):
    c=i%2
    for j in range (i):
            print(c,end=" ")
            if c==1:
                  c=0
            else:
                  c=1

    print()