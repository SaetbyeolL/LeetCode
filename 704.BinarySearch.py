# https://leetcode.com/problems/binary-search/description/

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (right + left) // 2 # 5
        
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
            
                
sol = Solution()
nums1  = [-1,0,3,5,9,12]
target1 = 9
print(sol.search(nums1, target1))
nums2  = [-1,0,3,5,9,12]
target2 = 6
print(sol.search(nums2, target2))