# Write a function that takes in a Binary Tree and returns its max path sum.
# A path is a collection of connected nodes where no node is connected to more than two other nodes;
# a path sum is the sum of the values of the nodes in a particular path.
# Each Binary Tree node has a value stored in a property
# called "value" and two children nodes stored in properties called "left" and "right," respectively.
# Children nodes can either be Binary Tree nodes themselves or the None (null) value.

# Sample input:
#            1
#          /   \
#         2     3
#        / \   / \
#       4  5   6  7

# Sample output: 18


def maxPathSum(tree):
    _, max_sum = find_max_sum(tree)
    return max_sum


def find_max_sum(tree):
    if not tree:
        return 0, 0

    left_max_sum_branch, left_max_path_sum = find_max_sum(tree.left)
    right_max_sum_branch, right_max_path_sum = find_max_sum(tree.right)
    value = tree.value

    max_child_sum_branch = max(left_max_sum_branch, right_max_sum_branch)
    max_sum_branch = max(max_child_sum_branch + value, value)
    max_sum_root_node = max(max_sum_branch, left_max_sum_branch + right_max_sum_branch + value)
    max_path_sum = max(max_sum_root_node, left_max_path_sum, right_max_path_sum)

    return max_sum_branch, max_path_sum
