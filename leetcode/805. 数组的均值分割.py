# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/23 下午11:56

# 给定的整数数组 A ，我们要将 A数组 中的每个元素移动到 B数组 或者 C数组中。（B数组和C数组在开始的时候都为空）
#
# 返回true ，当且仅当在我们的完成这样的移动后，可使得B数组的平均值和C数组的平均值相等，并且B数组和C数组都不为空。
#
# 示例:
# 输入:
# [1,2,3,4,5,6,7,8]
# 输出: true
# 解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
# 注意:
#
# A 数组的长度范围为 [1, 30].
# A[i] 的数据范围为 [0, 10000].
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/split-array-with-same-average
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
class Solution:
	def splitArraySameAverage(self, A: List[int]) -> bool:
if __name__ == "__main__":
	pass