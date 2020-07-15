# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/15 下午2:56
# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
#
# 例如，
#
# 给定二叉搜索树:
#
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# 和值: 2
# 你应该返回如下子树:
#
#       2
#      / \
#     1   3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-a-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
class Solution:
	def searchBST(self, root: TreeNode, val: int) -> TreeNode:
		if not root:
			return None
		if root.val > val:
			return self.searchBST(root.left, val)
		elif root.val < val:
			return self.searchBST(root.right, val)
		else:
			return root

# 迭代
class SolutionIter:
	def searchBST(self, root: TreeNode, val: int) -> TreeNode:
		while root:
			if root.val == val:
				return root
			elif root.val < val:
				root = root.right
			else:
				root = root.left
		return None

if __name__ == "__main__":
	pass