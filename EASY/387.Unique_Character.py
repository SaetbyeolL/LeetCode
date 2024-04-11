# https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i in dic:
            if dic[i] == 1:
                return s.index(i)
            else:
                continue
        return -1


# Test
sol = Solution()
s1 = "leetcode"
print(sol.firstUniqChar(s1)) #0
s2 = "loveleetcode"
print(sol.firstUniqChar(s2)) #2
s3 = "aabb"
print(sol.firstUniqChar(s3)) #-1













