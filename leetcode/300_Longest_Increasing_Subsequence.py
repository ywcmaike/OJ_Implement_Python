# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午8:26

# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?


# idea
# dp[i] 表示以nums[i]结尾的最长上升子序列的长度
#
# if nums[i] 比前面所有的元素小, dp[i]==1
# else: dp[i] = max(dp[j], dp[k], dp[p]....) + 1
# max(dp)

from typing import List

class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		if len(nums) < 1:
			return 0
		dp = []
		result = 1
		for i in range(len(nums)):
			dp.append(1)
			for j in range(i):
				if nums[j] < nums[i]:
					dp[i] = max(dp[j] + 1, dp[i])
			result = max(result, dp[i])
		return result


# nlog(n)  https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# 1.如果在活动列表的所有最终候选中A [i]最小，我们将开始新的长度为1的活动列表。
# 2.如果在活动列表的所有最终候选中A [i]最大，我们将克隆最大的活动列表，并将其扩展A [i]。
# 3.如果介于A [i]之间，我们将找到一个列表，该列表的最大结束元素小于A [i]。 克隆此列表并将其扩展A [i]。 我们将丢弃所有与此修改列表长度相同的其他列表。
def lengthOfLIS(self, nums):
	if len(nums) < 2: return len(nums)

	lists, ends = [[nums[0]]], [nums[0]]
	for i in range(len(nums)):
		if nums[i] < min(ends):
			lists[0][0] = nums[i]
			ends[0] = nums[i]
		elif nums[i] > max(ends):
			lists.append(lists[-1] + [nums[i]])
			ends.append(nums[i])
		else:
			j = self.findIndex(ends, nums[i])
			lists[j] = lists[j - 1] + [nums[i]]
			ends[j] = nums[i]
	return len(ends)


def findIndex(self, ends, key):
	l, r = 0, len(ends) - 1
	while r > l + 1:
		mid = (l + r) // 2
		if ends[mid] >= key:
			r = mid
		else:
			l = mid
	return r

if __name__ == "__main__":
	nums = [10,9,2,5,3,7,101,18]
	print(Solution().lengthOfLIS(nums))