def nNumbersSum(n):
    if n<1:
        return 0
    return n+nNumbersSum(n-1)
print(nNumbersSum(3))