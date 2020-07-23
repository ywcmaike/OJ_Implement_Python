# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/23 下午10:21

# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。
#
# 注意：本题相对原题做了扩展
#
# 示例:
#
#  输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/eight-queens-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
	def solveNQueens(self, n: int) -> List[List[str]]:
		board = [['.']*n for _ in range(n)]
		res = []
		def backtrack(left_diag, right_diag, column):
			j = len(column)
			if len(column) == n:
				tmp = []
				for k in board:
					tmp.append(''.join(k))
				res.append(tmp)
			for i in range(n):
				if i in column or i-j in left_diag or i+j in right_diag:
					continue
				board[i][j] = 'Q'
				backtrack(left_diag+[i-j], right_diag+[i+j], column+[i])
				board[i][j] = '.'
		backtrack([], [], [])
		return res



if __name__ == "__main__":
	print(Solution().solveNQueens(4))
	pass