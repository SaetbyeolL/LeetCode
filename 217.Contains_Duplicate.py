# https://leetcode.com/problems/contains-duplicate/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given an integer array 'nums', return 'true' if any value appears at least twice in the array,
# and return 'false' if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container = set()
        
        for i in nums:
            if i in container:
                return True
            else:
                container.add(i)
                
        return False
    

# Test
sol = Solution()
nums1 = [1,2,3,1]
print(sol.containsDuplicate(nums1))
nums2 = [1,2,3,4]
print(sol.containsDuplicate(nums2))
nums3 = [1,1,1,3,3,4,3,2,4,2]
print(sol.containsDuplicate(nums3))























