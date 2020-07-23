# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/23 下午9:19

# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#  
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-change
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import functools
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		@functools.lru_cache(amount)
		def dp(rem):
			if rem < 0: return -1
			if rem == 0: return 0
			mini = int(1e9)
			for coin in self.coins:
				res = dp(rem-coin)
				if res >= 0 and res < mini:
					mini = res + 1
			return mini if mini < int(1e9) else -1
		self.coins = coins
		if amount < 1:
			return 0
		return dp(amount)


if __name__ == "__main__":
	pass