def isPalindrome(n):
    i='true'
    original=n
    reverse=0

    while n>0:
        last_digit=n%10
        reverse=(reverse*10)+last_digit
        n=n//10
    if reverse!=original:
        i='false'
    return i
print(isPalindrome(1234321))