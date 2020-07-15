# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/15 下午3:06
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
#
# 示例:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
#
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#
#     5
#    / \
#   2   6
#    \   \
#     4   7
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea
# 我们要删除BST的一个节点，首先需要找到该节点。而找到之后，会出现三种情况。
# 1、待删除的节点左子树为空，让待删除节点的右子树替代自己。
# 2、待删除的节点右子树为空，让待删除节点的左子树替代自己
# 3、如果待删除的节点的左右子树都不为空。我们需要找到比当前节点小的最大节点（前驱），来替换自己
# 或者比当前节点大的最小节点（后继），来替换自己。
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
		if not root:
			return None
		if key < root.val:
			root.left = self.deleteNode(root.left, key)
			return root
		if key > root.val:
			root.right = self.deleteNode(root.right, key)
			return root
		if not root.right:
			return root.left
		if not root.left:
			return root.right
		minNode = root.right
		while minNode.left:
			minNode = minNode.left
		root.val = minNode.val

		def deleteMinNode(root: TreeNode):
			if not root.left:
				pRight = root.right
				root.right = None
				return pRight
			root.left = deleteMinNode(root.left)
			return root
		root.right = deleteMinNode(root.right)
		return root



if __name__ == "__main__":
	pass