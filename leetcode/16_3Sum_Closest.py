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
		distance = float("inf")
		if len(nums) < 3:
			return -1
		nums.sort()
		all_sum = sum(nums[:3])
		for i in range(len(nums) - 2):
			L = i + 1
			R = len(nums) - 1
			while L < R:
				cur_sum = nums[i] + nums[L] + nums[R]
				if abs(cur_sum - target) < distance:
					distance = abs(cur_sum - target)
					allsum = cur_sum
				if cur_sum < target:
					L += 1
				elif cur_sum > target:
					R -= 1
				else:
					return cur_sum
		return allsum


# 给定一个长度为n的数组和一个整数M，在这个数组里选择三个数，三个数的和小于等于M，返回有多少种方法(大疆笔试题)
class SolutionDJ:
	def threeSumSmallerThanM(self, nums:List[int], target:int) -> int:
		length = len(nums)
		if length < 3:
			return 0
		nums.sort()
		dup = [0] * length
		count = 0
		for i in range(1, length):
			if nums[i] == nums[i-1]:
				dup[i] = dup[i-1] + 1
			else:
				dup[i] = dup[i-1]
		for i in range(length -2):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			L = i+1
			R = length - 1
			while L < R:
				if nums[L] == nums[L-1] and L != i+1:
					L += 1
					continue
				cur_sum = nums[i] + nums[L] + nums[R]
				if cur_sum <= target:
					count = count + R - L - (dup[R] - dup[L])
					if nums[L] == nums[L + 1]:
						count += 1
					L += 1
				else:
					R -= 1
		return count

if __name__ == "__main__":
	# nums = [-1, 2, 1, -4]
	# target = 1
	# print(Solution().threeSumClosest(nums, target))

	nums = [3,2,5,2,1,4,2,3]
	target = 10
	print(SolutionDJ().threeSumSmallerThanM(nums, target))

	pass