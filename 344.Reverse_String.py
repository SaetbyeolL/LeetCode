# https://leetcode.com/problems/reverse-string/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with 0(1) extra memory.

from typing import List


# solution 1
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        

# solution 2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


# Test
sol = Solution()
s1 = ["h","e","l","l","o"]
print(sol.reverseString(s1))
s2 = ["H","a","n","n","a","h"]
print(sol.reverseString(s2))















