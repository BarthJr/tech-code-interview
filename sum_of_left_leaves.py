# https://leetcode.com/problems/sum-of-left-leaves/

# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0
    elif root.left and not root.left.left and not root.left.right:
        return root.left.val + sumOfLeftLeaves(root.right)
    else:
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)
