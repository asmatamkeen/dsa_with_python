def palindrome(s):
    s1=s
    def recursion(i):
        if i >= len(s)/2:
              return True
        if s[i]!=s[len(s)-i-1]:
              return False
        return recursion(i+1)
            
    return recursion(0)
print(palindrome("hannah"))

