from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Helper function to print the tree (for testing purposes)
def print_tree(root: Optional[TreeNode]):
    if root is None:
        return
    print(root.val, end=' ')
    print_tree(root.left)
    print_tree(root.right)

# Example usage
if __name__ == "__main__":
    # Create a sample tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Original tree:")
    print_tree(root)
    print("\n")

    # Invert the tree
    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("Inverted tree:")
    print_tree(inverted_root)
    print("\n")