# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

# Helper function to insert nodes into the BST
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

# Helper function to find a node in the BST
def find_node(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return find_node(root.left, val)
    return find_node(root.right, val)

# Example usage
if __name__ == "__main__":
    # Create a binary search tree
    values = [6, 2, 8, 0, 4, 7, 9, 3, 5]
    root = None
    for val in values:
        root = insert_into_bst(root, val)

    # Find nodes p and q
    p = find_node(root, 2)
    q = find_node(root, 8)

    # Find the lowest common ancestor
    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"The lowest common ancestor of {p.val} and {q.val} is {lca.val}")