# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: [TreeNode])-> int:
        if not root:
            return 0
        
        stack = [(root, 1)] # node, depth
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            
            # LIFO: The left child node is executed after the right child node is all processed
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        
        return max_depth
        
        
# test
sol = Solution()
# root1 = [3,9,20,null,null,15,7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(sol.maxDepth(root1))

# root2 = [1,null,2]
root2 = TreeNode(1)
root2.right = TreeNode(2)
print(sol.maxDepth(root2))
















