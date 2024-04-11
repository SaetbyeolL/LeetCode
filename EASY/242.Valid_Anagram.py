# https://leetcode.com/problems/valid-anagram/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An anagram is a word or phrase formed by rearranging the letters of a different word of phrase, 
# typically using all the original letters exactly once.


# solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [char for char in s]
        t_list = [char for char in t]
        
        for i in s_list:
            if i in t_list:
                t_list.remove(i)
        
        if t_list:
            return False
        else:
            return True


# solution 2
from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# solution 3
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return all(count == 0 for count in char_count.values())

# Test
sol = Solution()
s1 = "anagram"
t1 = "nagaram"
print(sol.isAnagram(s1, t1))
s2 = "rat"
t2 = "car"
print(sol.isAnagram(s2, t2))























