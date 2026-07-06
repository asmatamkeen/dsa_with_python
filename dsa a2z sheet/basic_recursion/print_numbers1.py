def printNumbers(n):
    if n<1:
        return 
    print(n)
    printNumbers(n-1)
printNumbers(7)