# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/23 下午8:41

# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
#
# 示例 1:
#
# 输入: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# 输出: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
# 示例 2:
#
# 输入: [3,1,4,null,null,2]
#
#   3
#  / \
# 1   4
#    /
#   2
#
# 输出: [2,1,4,null,null,3]
#
#   2
#  / \
# 1   4
#    /
#   3
# 进阶:
#
# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/recover-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def recoverTree(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		def find_two_swapped(root: TreeNode):
			nonlocal x, y, pred
			if not root:
				return
			find_two_swapped(root.left)
			if pred and root.val < pred.val:
				y = root
				if not x:
					x = pred
				else:
					return
			pred = root
			find_two_swapped(root.right)
		x = y = pred = None
		find_two_swapped(root)
		x.val, y.val = y.val, x.val

if __name__ == "__main__":
	pass