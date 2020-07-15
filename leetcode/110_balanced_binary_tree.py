#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/6/25 上午1:01

# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.


# idea 首先判断子树是否平衡，然后比较子树高度判断父节点是否平衡。算法如下：
#
# 检查子树是否平衡。如果平衡，则使用它们的高度判断父节点是否平衡，并计算父节点的高度。
# https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def isBalancedHelper(root: TreeNode) -> (bool, int):
            if not root:
                return True, -1
            leftIsBalanced, leftHeight = isBalancedHelper(root.left)
            if not leftIsBalanced:
                return False, 0
            rightIsBalanced, rightHeight = isBalancedHelper(root.right)
            if not rightIsBalanced:
                return False, 0
            return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        return isBalancedHelper(root)[0]


if __name__ == "__main__":
    pass
