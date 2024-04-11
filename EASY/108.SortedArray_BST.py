# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given an integer array 'nums' where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree. nums is sorted in a strictly increasing order


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



from typing import List
class Solution:
    def sortedArrayToBST(self, nums: List[int])->List[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2                              # Find the middle value 
        root = TreeNode(nums[mid])                        # Root node of each subtree within a recursive function
        
        root.left = self.sortedArrayToBST(nums[:mid])     # Recursively call with the left subarray based on the middle value
        root.right = self.sortedArrayToBST(nums[mid+1:])  # Recursively call with the right subarray based on the middle value
        
        return root
        
        


# Test case
sol = Solution()
nums1 = [-10,-3,0,5,9]
print(sol.sortedArraToBST(nums1))

nums2 = [1,3]
print(sol.sortedArrayToBST(nums2))

























