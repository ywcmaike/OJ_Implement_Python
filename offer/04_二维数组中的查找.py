# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/12 下午11:06

# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
#  
#
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# idea
# 从右上角开始走，利用这个顺序关系可以在O(m+n)的复杂度下解决这个题：
#
# 如果当前位置元素比target小，则row++
# 如果当前位置元素比target大，则col--
# 如果相等，返回true
# 如果越界了还没找到，说明不存在，返回false

from typing import List
class Solution:
	def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
		m = len(matrix)
		if m < 1:
			return False
		n = len(matrix[0])
		if n < 1:
			return False
		row, col = 0, n-1
		while row < m and col >= 0:
			if matrix[row][col] < target:
				row += 1
			elif matrix[row][col] > target:
				col -= 1
			else:
				return True
		return False

if __name__ == "__main__":
# 	matrix = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
	matrix = [[]]
	target = 0
	# target = 2
	# target = 32
	print(Solution().findNumberIn2DArray(matrix, target))
	pass