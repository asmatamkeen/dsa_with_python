a=int(input("Enter number of rows:"))
for i in range(1,a+1):
    for ch in range(ord('A'),ord("A")+i):
        print(chr(ch),end=' ')
    print()