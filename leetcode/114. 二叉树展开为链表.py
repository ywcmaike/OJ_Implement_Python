#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/8/2 下午11:27

# 给定一个二叉树，原地将它展开为一个单链表。
#
#  
#
# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 寻找前驱节点
# 如果当前节点的左节点存在，寻找左子树的最右的节点，作为当前节点的右节点的前驱节点，
# 操作： 当前节点的前驱节点指向右子节点，当前节点左节点为空，
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                precess = nxt = curr.left
                while precess.right:
                    precess = precess.right
                precess.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right

if __name__ == '__main__':
    pass
