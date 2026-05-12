def isPalindrome(x):
        reversed_num=''
        original_num=x
        if (x == 0):
            return True
        else:
            while (x>0):
                last_digit=x%10
                x=int(x/10)
                reversed_num=reversed_num+str(last_digit)
            if str(original_num) == reversed_num:
                return True
            else:
                return False
print(isPalindrome(0))