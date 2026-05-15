class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        substr_s = ''
        
        for end, char in enumerate(s):
            if char not in substr_s:
                substr_s = substr_s + char
            else:
                index = substr_s.index(char)
                substr_s = substr_s[index + 1:] + char
                
            if len(substr_s) > max_length:
                max_length = len(substr_s)
                
        return max_length
        