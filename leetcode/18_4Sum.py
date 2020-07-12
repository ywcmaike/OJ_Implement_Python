# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/12 下午6:24

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


from typing import List

class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		result = []
		length = len(nums)
		if length < 4:
			return result
		nums.sort()
		# print(nums)
		for i in range(length - 3):
			if i != 0 and nums[i-1] == nums[i]:
				continue
			for j in range(i+1, length-2):
				if j != i+1 and nums[j] == nums[j-1]:
					continue
				L = j + 1
				R = length - 1
				while L < R:
					if L != j+1 and nums[L] == nums[L-1]:
						L += 1
						continue
					if R != length-1 and nums[R] == nums[R+1]:
						R -= 1
						continue
					cursum = nums[i] + nums[j] + nums[L] + nums[R]
					if cursum == target:
						result.append([nums[i], nums[j], nums[L], nums[R]])
						L += 1
						R -= 1
					elif cursum < target:
						L += 1
					else:
						R -= 1
		return result






if __name__ == "__main__":
	nums = [1, 0, -1, 0, -2, 2]
	target = 0
	print(Solution().fourSum(nums, target))
	pass