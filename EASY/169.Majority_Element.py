# https://leetcode.com/problems/majority-element/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than [n/2] times.
# You may assume that the majority element always exists in the array.

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        for num, count in counts.items():
            if count > len(nums) // 2:
                return num


# Test
sol = Solution()
nums1 = [3,2,3]
print(sol.majorityElement(nums1))
nums2 = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums2))




