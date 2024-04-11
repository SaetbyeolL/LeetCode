# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given an integer array 'nums' sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. The return the number of unique elements in nums.
# Consider the number of unique elements of 'nums' to be 'k', to get accepted, you need to do the following things: 
# change the array 'nums' such that the first 'k' elements of 'nums' contain the unique elements in the order they were present in 'nums' initially.
# The remaining elements of 'nums' are not important as well as the size of 'nums'.
# Return 'k'.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
    
    
    
    
    
#1) 
        from typing import List

        class Solution:
            def removeDuplicates(self, nums: List[int]) -> int:
                
                if not nums: # check if the array is empty
                    return 0
                
                uniqueCount = 1 # initialize a counter for unique elements, assuming the first element is always unique
                
                for i in range(1, len(nums)): #iterate through the array starting from the second element
                    if nums[i] != nums[i-1]: # check if the current element is different from the previous one
                        nums[uniqueCount] = nums[i] # if it's not a duplicate, update the array at the position indicated by the uniqueCount
                        uniqueCount += 1 # increment the uniqueCount
                        
                # for i in range(uniqueCount, len(nums)):
                # nums[i] = '_'
                
                return uniqueCount
    
 
 
#test case
sol = Solution()
nums1 = [1,1,2]
k1 = sol.removeDuplicates(nums1)
print(k1, nums1[:k1])

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = sol.removeDuplicates(nums2)
print(k2, nums2[:k2])



































