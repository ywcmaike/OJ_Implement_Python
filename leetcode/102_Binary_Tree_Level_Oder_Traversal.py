#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/10 下午11:51


# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level + 1, res)
        self.dfs(root.right, level + 1, res)

from collections import deque

class SolutionBFS:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodes = []
        nodeDeque = deque([root])
        while nodeDeque:
            levelLen = len(nodeDeque)
            levelNodes = []
            for i in range(levelLen):
                curNode = nodeDeque.popleft()
                levelNodes.append(curNode.val)
                if curNode.left:
                    nodeDeque.append(curNode.left)
                if curNode.right:
                    nodeDeque.append(curNode.right)
            nodes.append(levelNodes)
        return nodes