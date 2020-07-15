# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午3:31

# problems: 222. Count Complete Tree Nodes
# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
#
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea
# 如果二叉树中除了叶子结点，每个结点的度都为 2，则此二叉树称为满二叉树
# （二叉树的度代表**某个结点的孩子或者说直接后继的个数。**对于二叉树而言，1度是只有一个孩子或者说单子树,2度是有两个孩子或者说左右子树都有。）
# 如果二叉树中除去最后一层节点为满二叉树，且最后一层的结点依次从左到右分布，则此二叉树被称为完全二叉树。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def countNodes(self, root: TreeNode) -> int:
		if root:
			return 1 + self.countNodes(root.right) + self.countNodes(root.left)
		else:
			0

if __name__ == "__main__":
	pass