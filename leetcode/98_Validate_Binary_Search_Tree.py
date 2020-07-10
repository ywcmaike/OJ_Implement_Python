#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/11 上午12:16

#  Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false

# Explanation: The root node's value is 5 but its right child's value is 4.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_num = float("-inf")
        max_num = float("inf")
        if not root:
            return True

        def isBST(root, min_num, max_num):
            if not root:
                return True
            if min_num >= root.val or root.val >= max_num:
                return False
            return isBST(root.left, min_num, root.val) and isBST(root.right, root.val, max_num)

        return isBST(root, min_num, max_num)


## in order

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre, cur, stack = None, root, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            s = stack.pop()
            if pre and s.val <= pre.val:
                return False
            pre, cur = s, s.right
        return True