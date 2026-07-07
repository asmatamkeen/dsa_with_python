def fibonacci(n):
    if n<=1:
        return n
    f1=fibonacci(n-1)
    f2=fibonacci(n-2)
    return f1+f2
print(fibonacci(5))
    