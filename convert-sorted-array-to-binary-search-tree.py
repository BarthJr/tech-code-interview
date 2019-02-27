# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def sortedArrayToBST(nums: 'List[int]') -> 'TreeNode':
    if not nums:
        return None
    mid = len(nums) // 2 if len(nums) % 2 == 1 else (len(nums) - 1) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root
