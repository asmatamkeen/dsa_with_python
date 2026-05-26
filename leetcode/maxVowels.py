def maxVowels(s,k):
    vowels = 'aeiou'
    max_vowels = 0
    for i in range(k):
        if s[i] in vowels:
            max_vowels += 1
    current_vowels = max_vowels

    for j in range(k, len(s)):
        if s[j-k] in vowels:
            current_vowels -= 1
        
        if s[j] in vowels:
            current_vowels += 1
        
        max_vowels = max(max_vowels, current_vowels)
    return max_vowels

print(maxVowels("abciiidef",3))