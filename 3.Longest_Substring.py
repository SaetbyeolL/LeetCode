# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given a string 's', find the length of the longest substring without repaeting characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()                                   # character set
        start = 0                                          # start index
        max_length = 0                                     # maximum substring length
        
        for end in range(len(s)):
            while s[end] in char_set:                      # If the current character already exists in the set
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])                           # Add current character to set
            max_length = max(max_length, end - start + 1)  # Calculate length of substring so far
        
        return max_length
        
        
        
        
        
        
        
        
        





# Test
s1 = "abcabcbb"
print(lengthOfLongestSubstring(s1))
s2 = "bbbbb"
print(lengthOfLongestSubstring(s2))
s3 = "pwwkew"
print(lengthOfLongestSubstring(s3))















