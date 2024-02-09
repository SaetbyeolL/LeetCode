# https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

from typing import List
# Definition for a binary tree node.
class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val  
        self.left = left 
        self.right = right  

class Solution:  
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # Initialize a list to store the result
        stack = []  # Initialize a stack to store nodes
        current_node = root  
        
        while current_node or stack:  
            while current_node:  
                stack.append(current_node)        # Push the current node onto the stack
                current_node = current_node.left  # Move to the left child node
                
            current_node = stack.pop()            # Pop a node from the stack and set it as the current node
            result.append(current_node.val)       # Append the value of the current node to the result list
            current_node = current_node.right     # Move to the right child node
        return result

# Test
sol = Solution()
# root1 = [1, null, 2, 3]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(sol.inorderTraversal(root1))
# root2 = []
root2 = None
print(sol.inorderTraversal(root2))
# root3 = [1]
root3 = TreeNode(1)
print(sol.inorderTraversal(root3))












