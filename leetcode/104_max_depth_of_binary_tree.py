#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/6/25 上午12:27

# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 迭代
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

# 递归， 使用stack
class SolutionStack:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))
        height = 0

        while stack != []:
            current_height, current_node = stack.pop()
            if current_node is not None:
                height = max(height, current_height)
                stack.append((current_height + 1, current_node.left))
                stack.append((current_height + 1, current_node.right))
        return height


if __name__ == '__main__':
    binary_tree = [3, 9, 20, None, None, 15, 7]



