def longestCommonPrefix(strs):
        if not strs:
            return ""
            
        strs.sort()
        s1 = strs[0]
        s2 = strs[-1] 
        common = ""
        for i in range(len(s1)): 
            if i < len(s2) and s1[i] == s2[i]:
                common += s1[i]
            else:
                return common

        return common
        

print(longestCommonPrefix(["",'']))