#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/6/25 上午1:01


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

