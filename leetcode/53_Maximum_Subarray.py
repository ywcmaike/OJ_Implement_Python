# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午8:06


# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# idea
# dp = max(dp[i-1]+nums[i], nums[i])

from typing import List

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		dp = []
		for i in range(len(nums)):
			if i == 0:
				dp.append(nums[0])
			else:
				dp.append(max(nums[i], nums[i] + dp[i-1]))
		return max(dp)

if __name__ == '__main__':
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print(Solution().maxSubArray(nums))