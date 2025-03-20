from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
        return valid(root, float('-inf'), float('inf'))

# Example usage:
# Construct a binary tree
#     2
#    / \
#   1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# Create an instance of Solution and check if the tree is a valid BST
solution = Solution()
print(solution.isValidBST(root))  # Output: True