# https://leetcode.com/problems/symmetric-tree/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# given the root of a binary tree, check whether it is a mirror of itself(i.e. symmetric around its center)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            left_node, right_node = stack.pop()
            
            if not left_node and not right_node:
                continue
            if not left_node or not right_node or left_node.val != right_node.val:
                return False
            
            stack.append((left_node.left, right_node.right))
            stack.append((left_node.right, right_node.left))
        
        return True
        
# test)
sol = Solution()
# root1 = [1,2,2,3,4,4,3]
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right = TreeNode(2)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)
print(sol.isSymmetric(root1))

# root2 = [1,2,2,null,3,null,3]
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)
print(sol.isSymmetric(root2))