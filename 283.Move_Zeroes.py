# https://leetcode.com/problems/move-zeroes/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1
                
            


# Test
sol = Solution()
nums1 = [0,1,0,3,12]
print(sol.moveZeroes(nums1))
nums2 = [0]
print(sol.moveZeroes(nums2))






