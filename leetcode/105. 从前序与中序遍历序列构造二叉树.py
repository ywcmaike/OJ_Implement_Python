# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/23 下午8:18
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
		n = len(preorder)
		index = {element: i for i, element in enumerate(inorder)}
		def myBuildTruee(preorder_left, preorder_right, inorder_left, inorder_right):
			if preorder_left > preorder_right:
				return None
			preorder_root = preorder_left
			inorder_root = index[preorder[preorder_root]]

			root = TreeNode(preorder[preorder_root])
			size_left_subtree = inorder_root - inorder_left
			root.left = myBuildTruee(preorder_left+1, preorder_left+size_left_subtree, inorder_left, inorder_root-1)
			root.right = myBuildTruee(preorder_left+size_left_subtree+1, preorder_right, inorder_root+1, inorder_right)
			return root
		return myBuildTruee(0, n-1, 0, n-1)


if __name__ == "__main__":
	pass