# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午9:12

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


# 定义状态
# 总结状态转移方程
# 分析状态转移方程不能满足的特殊情况。
# 得到最终解
# dp[i][j]=min(dp[i-1][j], dp[i-1],[j-1])+tri[i][j]
# dp[1][0]=tri[1][0]+tri[0][0]
# dp[1][1]=tri[1][1]+tri[0][0]
# max(dp[l, 0], dp[l,1], ....dp[l, l]

from typing import List
class Solution:
	def minimumTotal(self, triangle: List[List[int]]) -> int:
		if len(triangle) < 1:
			return 0
		if len(triangle) == 1:
			return triangle[0][0]
		triangle[0][0] = triangle[0][0]
		triangle[1][0] = triangle[1][0] + triangle[0][0]
		triangle[1][1] = triangle[1][1] + triangle[0][0]
		for i in range(2, len(triangle)):
			for j in range(len(triangle[i])):
				if j == 0:
					triangle[i][j] = triangle[i-1][j] + triangle[i][j]
				elif j == len(triangle[i])-1:
					triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
				else:
					triangle[i][j] = min(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]
		return min(triangle[-1][:])

# fast:


if __name__ == "__main__":
	triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
	print(Solution().minimumTotal(triangle))
