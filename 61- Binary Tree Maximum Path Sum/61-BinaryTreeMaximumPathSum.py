from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            lmax = dfs(root.left)
            rmax = dfs(root.right)
            lmax = max(lmax, 0)
            rmax = max(rmax, 0)
            res[0] = max(res[0], root.val + lmax + rmax)
            return root.val + max(lmax, rmax)

        dfs(root)
        return res[0]

# Example usage:
# Construct the binary tree
#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create a Solution object and find the maximum path sum
sol = Solution()
print(sol.maxPathSum(root))  # Output: 6