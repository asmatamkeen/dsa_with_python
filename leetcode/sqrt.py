class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        else:
            left = 1
            right = (num // 2) 
            while left <= right:
                mid = (left + right) // 2
                guess = mid * mid

                if guess == num:
                    return True
                    
                elif guess > num:
                    right = mid-1
                else:
                    left = mid +1
            return  False       