# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/15 下午3:37


# 给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。
#
# 返回移除了所有不包含 1 的子树的原二叉树。
#
# ( 节点 X 的子树为 X 本身，以及所有 X 的后代。)
#
# 示例1:
# 输入: [1,null,0,0,1]
# 输出: [1,null,0,null,1]
#
# 解释:
# 只有红色节点满足条件“所有不包含 1 的子树”。
# 右图为返回的答案。
#
#
# 示例2:
# 输入: [1,0,1,0,0,0,1]
# 输出: [1,null,1,null,1]
#
#
#
# 示例3:
# 输入: [1,1,0,1,1,0,1,0]
# 输出: [1,1,0,1,1,null,1]
#
#
#
# 说明:
#
# 给定的二叉树最多有 100 个节点。
# 每个节点的值只会为 0 或 1 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-pruning
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea
# 在递归的过程中，如果当前结点的左右节点皆为空，且当前结点为0，我们就将当前节点剪掉即可。

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def pruneTree(self, root: TreeNode) -> TreeNode:

		def deal(node:TreeNode)->TreeNode:
			if not node:
				return None
			node.left = deal(node.left)
			node.right = deal(node.right)
			if not node.left and not node.right and node.val == 0:
				return None
			return node
		return deal(root)




if __name__ == "__main__":
	pass