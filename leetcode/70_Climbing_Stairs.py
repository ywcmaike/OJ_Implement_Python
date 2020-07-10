# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午7:39

# ou are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# idea
# dp f(n) = f(n-1) + f(n-1)

class Solution:
	def climbStairs(self, n: int) -> int:
		if n == 1:
			return 1
		dp = []
		dp.append(0)
		dp.append(1)
		dp.append(2)
		for i in range(3, n+1):
			dp.append(dp[i-1] + dp[i-2])
		return dp[n]

if __name__ == '__main__':
	print(Solution().climbStairs(3))