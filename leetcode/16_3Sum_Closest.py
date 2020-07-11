# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/11 下午6:27

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# idea
from typing import List

class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		distance = int("inf")
		if len(nums) < 3:
			return -1
		for i in range(len(nums) - 2)
		nums.sort()




		pass


if __name__ == "__main__":
	nums = [-1, 2, 1, -4]
	target = 1
	print(Solution().threeSumClosest(nums, target))


	pass