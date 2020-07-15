# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/15 下午12:38

# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。
#
#  
#
# 示例 1：
#
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
# 示例 2：
#
# 输入：grid = [[1,1,0,0]]
# 输出：1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-1-bordered-square
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 非递归的动态规划！
# dp是三维数组，第三维[0]就是左侧连续几个1，第三维[1]就是上面连续几个1。
# 从grid的左上角开始迭代，每次考虑grid[i][j]的左上角的正方形。
#


from typing import List
class Solution:
	def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
		m = len(grid)
		if m < 1:
			return 0
		n = len(grid[0])
		if n < 1:
			return 0
		dp = [[[1, 1] if grid[i][j]==1 else [0, 0] for j in range(n)] for i in range(m)]
		largest_len = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 0:
					continue
				if j != 0:
					dp[i][j][0] += dp[i][j-1][0]
				if i != 0:
					dp[i][j][1] += dp[i-1][j][1]

				if dp[i][j][0] > largest_len and dp[i][j][1] > largest_len:
					length_max = min(dp[i][j][0], dp[i][j][1])
					for length in range(largest_len+1, length_max+1):
						if dp[i][j+1-length][1] >= length and dp[i+1-length][j][0] >= length:
							largest_len = length
		return largest_len**2



if __name__ == "__main__":
	grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
	print(Solution().largest1BorderedSquare(grid))
	pass