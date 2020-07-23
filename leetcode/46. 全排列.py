# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/23 下午10:19

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		n = len(nums)
		res = []
		def backtrack(first=0):
			if first == n:
				res.append(nums[:])
			for i in range(first, n):
				nums[first], nums[i] = nums[i], nums[first]
				backtrack(first+1)
				nums[first], nums[i] = nums[i], nums[first]
		backtrack()
		return res


if __name__ == "__main__":
	pass