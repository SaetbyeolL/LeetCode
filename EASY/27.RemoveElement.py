# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150


# Given an integer array 'nums' and ininteger 'val', remove all occurrences of 'val' in 'nums' in-place.
# The order of the elements may be changed. Then return the number of elements in 'nums' which are not equal to 'val'.
# Consider the number of elements in 'nums' which are not equal to 'val' be 'k', to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        









#test case
sol = Solution()
nums1 = [3,2,2,3]
val1 = 3
k1 = sol.removeElement(nums1, val1)
print(k1)

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
k1 = sol.removeElement(nums2, val2)
print(k2)


