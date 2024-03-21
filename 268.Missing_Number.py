# https://leetcode.com/problems/missing-number/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given an array 'nums' containing 'n' distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

from typing import List
#solution 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        list = []
        
        for i in range(0, len(nums)+1):
            list.append(i)
        
        for i in list:
            if i in nums:
                continue
            else:
                return i
        
        
#solution 2       
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum


        
# Test
sol = Solution()
nums1 = [3,0,1]
print(sol.missingNumber(nums1))
nums2 = [0,1]
print(sol.missingNumber(nums2))
nums3 = [9,6,4,2,3,5,7,0,1]
print(sol.missingNumber(nums3))
























