# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/23 下午2:53
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意:
#
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 示例 1:
#
# 输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#  
#
# 示例 2:
#
# 输入: [1, 2, 3, 5]
#
# 输出: false
#
# 解释: 数组不能分割成两个元素和相等的子集.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		all_sum, length = sum(nums), len(nums)
		if all_sum % 2 != 0:
			return False
		half_sum = all_sum // 2
		dp = [[False]*(half_sum+1) for _ in range(length+1)]
		for i in range(length+1):
			if i == 0:
				dp[i][0] = True
			for j in range(1, half_sum+1):
				if j - nums[i-1] < 0:
					dp[i][j] = dp[i-1][j]
				else:
					dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
		return dp[length][half_sum]

	# def canPartition(self, nums: List[int]) -> bool:
	# 	all_sum, length = sum(nums), len(nums)
	# 	if all_sum % 2 != 0:
	# 		return False
	# 	half_sum = all_sum // 2
	# 	dp = [[False] * (half_sum+1)]
	# 	dp[0] = True
	# 	for i in range(length):
	# 		for j in range(half_sum, -1, -1):
	# 			if j - nums[i] >= 0:
	# 				dp[j] = dp[j] or dp[j - nums[i]]
	# 	return dp[half_sum]

if __name__ == "__main__":
	nums = [1, 5, 11, 5]
	# nums = [1, 2, 3, 5]
	print(Solution().canPartition(nums))
	pass