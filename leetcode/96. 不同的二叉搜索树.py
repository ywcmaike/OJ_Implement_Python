# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/16 上午1:18

# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def numTrees(self, n: int) -> int:
if __name__ == "__main__":
	pass