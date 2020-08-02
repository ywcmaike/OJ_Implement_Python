#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/8/2 下午11:32
# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:



if __name__ == '__main__':
    