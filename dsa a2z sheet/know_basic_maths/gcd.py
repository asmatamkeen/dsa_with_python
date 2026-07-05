def GCD(n1,n2):
        while n1 > 0 and n2 > 0:
            if n1 > n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1
        
        return n1 if n1 > 0 else n2

print(GCD(4,6))