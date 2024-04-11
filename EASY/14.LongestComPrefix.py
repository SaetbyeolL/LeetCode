# https://leetcode.com/problems/longest-common-prefix/description/?envType=featured-list&envId=top-100-liked-questions?envType=featured-list&envId=top-100-liked-questions

# 14. Longest Common Prefix
# write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string"".

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: # strs is empty or not
            return ""
        
        prefix = strs[0] # set 1st string as comparison target
        
        for i in range(len(prefix)): # loop all prefix's char each to compare other strings
            for char in strs[1:]: # we already set 1st string as "prefix". So, compare char from 2nd string
                if i >= len(char) or prefix[i] != char[i]:
                    # char's length is less than i, means there is no character that it cannot compare.
                    # compare all characters each and if it does not match, return only matching characters
                    return prefix[:i]
        
        return prefix # if all characters are same, return prefix
                                                          
            
        
# ex) 
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["flower","flow","flight"]))


