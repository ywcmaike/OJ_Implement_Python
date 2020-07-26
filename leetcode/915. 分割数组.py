# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/23 下午11:56

# 给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 left 和 right， 使得：
#
# left 中的每个元素都小于或等于 right 中的每个元素。
# left 和 right 都是非空的。
# left 要尽可能小。
# 在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。
#
#  
#
# 示例 1：
#
# 输入：[5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]
# 示例 2：
#
# 输入：[1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/partition-array-into-disjoint-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
class Solution:
	def partitionDisjoint(self, A: List[int]) -> int:
if __name__ == "__main__":
	pass