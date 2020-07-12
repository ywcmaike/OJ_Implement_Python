# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/12 下午10:26

# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1
# and the result is guaranteed to be at most 231 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

from typing import List


class Solution:
	def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
		AB_dict = {}
		length = len(A)
		count = 0
		for i in range(length):
			for j in range(length):
				if A[i] + B[j] not in AB_dict:
					AB_dict[A[i] + B[j]] = 1
				else:
					AB_dict[A[i] + B[j]] += 1

		for i in range(length):
			for j in range(length):
				count += AB_dict.get(-C[i]-D[j], 0)
		return count

if __name__ == "__main__":
	A = [ 1, 2]
	B = [-2,-1]
	C = [-1, 2]
	D = [ 0, 2]
	print(Solution().fourSumCount(A, B, C, D))
	pass