# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/13 下午9:24

# 给定一个正整数和负整数组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。
#
# 返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。
#
# 注意：本题相对书上原题稍作改动
#
# 示例:
#
# 输入:
# [
#    [-1,0],
#    [0,-1]
# ]
# 输出: [0,1,0,1]
# 解释: 输入中标粗的元素即为输出所表示的矩阵
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-submatrix-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
	def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
		m, n, res, rescood = len(matrix), len(matrix[0]), float('-inf'), []
		for cur in range(m):
			colsum = [0] * n
			for i in range(cur, m):
				for j in range(n):
					colsum[j] += matrix[i][j]
				rowsum = 0
				lefttop = [cur, 0]
				for k in range(n):
					if rowsum < 0:
						rowsum = 0
						lefttop = [cur, k]
					rowsum += colsum[k]
					if rowsum > res:
						res, rescood = rowsum, lefttop+[i, k]
		return rescood


if __name__ == "__main__":
	matrix = [
   [-1,0],
   [0,-1]
]
	print(Solution().getMaxMatrix(matrix))
	pass