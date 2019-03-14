# https://leetcode.com/problems/symmetric-tree/
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

"""
>>> root = TreeNode(1)
>>> root.left = TreeNode(2)
>>> root.right = TreeNode(2)
>>> root.left.left = TreeNode(3)
>>> root.left.right = TreeNode(4)
>>> root.right.left = TreeNode(4)
>>> root.right.right = TreeNode(3)

>>> root1 = TreeNode(1)
>>> root1.left = TreeNode(2)
>>> root1.right = TreeNode(2)
>>> root1.left.left = None
>>> root1.left.right = TreeNode(3)
>>> root1.right.left = None
>>> root1.right.right = TreeNode(3)

>>> isSymmetric(root)
True
>>> isSymmetric(root1)
False
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root: TreeNode) -> bool:
    queue = [(root, root)]
    while queue:
        node1, node2 = queue.pop()
        if not node1 and not node2:
            continue
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False
        queue.extend((
            (node1.left, node2.right),
            (node1.right, node2.left)
        ))
    return True
