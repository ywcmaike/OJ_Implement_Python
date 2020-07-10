# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/7 下午6:59

# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# idea
#
# 统计每个元素出现个数, map
#
# 若排好序, 两个指针移动


from typing import List
class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		dict_1 = {}
		dict_2 = {}
		result = []
		for i in nums1:
			if i not in dict_1:
				dict_1[i] = 1
			else:
				dict_1[i] += 1
		for j in nums2:
			if j not in dict_2:
				dict_2[j] = 1
			else:
				dict_2[j] += 1

		for k, v in dict_1.items():
			if k in dict_2:
				for i in range(min(v, dict_2[k])):
					result.append(k)
		return result

class SolutionSort:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		result = []
		i, j = 0, 0
		while i < len(nums1) and j < len(nums2):
			if nums1[i] == nums2[j]:
				result.append(nums1[i])
				i += 1
				j += 1
			elif nums1[i] < nums2[j]:
				i += 1
			else:
				j += 1
		return result
		pass

if __name__ == '__main__':

	# nums1 = [1, 2, 2, 1]
	# nums2 = [2, 2]
	# nums1 = [4, 9, 5]
	# nums2 = [9, 4, 9, 8, 4]
	# solution = Solution()
	# print(solution.intersect(nums1, nums2))

	# arr1 = [1, 2, 3, 4, 4, 13]
	# arr2 = [1, 2, 3, 9, 10]
	arr1 = [1, 3, 4, 4, 13]
	arr2 = [1, 4, 9, 10]
	solution = SolutionSort()
	print(solution.intersect(arr1, arr2))