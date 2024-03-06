# https://leetcode.com/problems/single-number/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given a non-empty array of integers 'nums', every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from typing import List


# solution 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        
        for i in nums:
            if i not in dic:
                dic[i] = True
            else:
                dic[i] = False
        
        for key, val in dic.items():
            if val == True: 
                return key
        
# solution 2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_counts = {}
        
        for i in nums:
            if i in num_counts: 
                num_counts[i] += 1
            else:
                num_counts[i] = 1
        
        for key, value in num_counts.items():
            if value == 1:
                return key
        

# test
sol = Solution()
nums1 = [2,2,1]
print(sol.singleNumber(nums1))
nums2 = [4,1,2,1,2]
print(sol.singleNumber(nums2))
nums3 = [1]
print(sol.singleNumber(nums3))

















