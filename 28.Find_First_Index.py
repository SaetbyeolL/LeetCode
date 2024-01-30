# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Find the index of the first occurence in a string

# Given two strings 'needle' and 'haystack', return the index of the first occurrence of 'needle' in 'haystack',
# or '-1' if 'needle' is not part of 'haystack'

# class Solution: 
#     def strStr(self, haystack: str, needle:  str) -> int:
        




# solution 1) 
class Solution: 
    def strStr(self, haystack: str, needle:  str) -> int:
        
        if not (haystack or needle): # if needle is an empty string, return 0 
            return 0 
        
        for i in range(len(haystack) - len(needle) + 1): # iterate through the haystack string
            if haystack[i:i+len(needle)] == needle: #check if substring of haystack starting at index i is equal to needle
                return i
        
        return -1 # if needle is not found in haystack, return -1
            
        

# solution 2)
class Solution: 
    def strStr(self, haystack: str, needle:  str) -> int:
        return haystack.find(needle); # Returns the index of the first occurrence of the substring



# Test code
sol = Solution()
haystack1, needle1 = "sadbutsad", "sad"
print(sol.strStr(haystack1, needle1))

haystack2, needle2 = "leetcode", "leeto"
print(sol.strStr(haystack2, needle2))
































