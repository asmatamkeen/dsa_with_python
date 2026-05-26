def countOdds(low,high):
    if low % 2 == 1 or high % 2 == 1:
        return abs(low - high) // 2 + 1
    else:
        return abs(low - high) // 2
    
print(countOdds(3, 7))