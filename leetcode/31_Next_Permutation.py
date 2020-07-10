# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午2:09

# problem: 31. 下一个排列
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# idea:
# 从后往前找到第一个【相邻升序对】，即A[i] < A[i + 1]。此时A[i + 1, end)为降序。
# 在区间[i + 1, end)中，从后往前找到第一个大于A[i]的元素A[j]
# 交换A[i]和A[j]，此时A[i + 1, end)一定还是降序，因为A[j]是从右侧起第一个大于A[i]的值
# 反转A[i + 1, end)，变成升序

from typing import List

class Solution:
	def nextPermutation(self, nums: List[int]) -> None:
		"""
        Do not return anything, modify nums in-place instead.
        """
		n = len(nums)
		if n < 2:
			# print(nums)
			return
		i = n - 1
		while i > 0 and nums[i-1] >= nums[i]:
			i -= 1
		if i == 0:
			nums[:] = nums[::-1]
			# print(nums)
			# return nums
		else:

			j = i - 1
			for k in range(n-1, i-1, -1):
				if nums[k] > nums[j]:
					nums[k], nums[j] = nums[j], nums[k]
					# temp = nums[i:]
					# nums[i:] = temp[::-1]
					nums[:] = nums[:i] + nums[i:][::-1]
					break
		# print(nums)




if __name__ == '__main__':
	# nums = [1, 2, 3]
	# nums = [3, 2, 1]
	# nums = [1, 1, 5]
	# nums = [5, 1, 1]
	nums = [1, 2, 3, 8, 5, 7, 5, 4]
	# nums = [1, 3, 2]
	print(nums)
	print(Solution().nextPermutation(nums))
	pass
