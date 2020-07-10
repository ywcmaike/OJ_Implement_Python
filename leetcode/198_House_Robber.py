# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午10:28

# 198. House Robber

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

# idea
# dp 小偷一定会从前偷到最后（强调：偷盗至第i个房间，不代表小偷要从第i个房间中获取财物）
# dp[i] = max(dp[i-1], dp[i-2]+nums[i])

from typing import List

class Solution:
	def rob(self, nums: List[int]) -> int:
		if len(nums) < 1:
			return 0
		elif len(nums) == 1:
			return nums[0]
		dp = []
		dp.append(nums[0])
		dp.append(max(nums[0], nums[1]))
		for i in range(2, len(nums)):
			dp.append(max(dp[i-1], dp[i-2]+nums[i]))
		return max(dp)

if __name__ == "__main__":
	# nums = [2, 7, 9, 3, 1]
	nums = [1, 2, 3, 1]
	print(Solution().rob(nums))