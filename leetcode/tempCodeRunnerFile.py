    while (num>0):
            last_digit=num%10
            num=int(num/10)
            reversed_num=reversed_num+str(last_digit)
        if str(original_num) == reversed_num:
            print(f"{original_num} is a palindrome")
        else:
            print(f"{original_num} is not a palindrome")