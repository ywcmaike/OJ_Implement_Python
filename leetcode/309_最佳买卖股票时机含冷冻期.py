# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/13 上午12:13

# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea
# 状态表示及转移
# dp[i][j]dp[i][j] 表示第 ii 天，持有股票的状态。dp[i][1]dp[i][1] 表示持有股票。
#
# dp[i][0]dp[i][0] 表示第 ii 天未持有股票
#
# 它可能是第 i-1i−1 天持有股票，然后第i天卖出去了，所以 dp[i][0] = dp[i-1][1] + price[i];dp[i][0]=dp[i−1][1]+price[i];
# 也可能是第 i-1i−1 天未持有股票，第i天没有买入，所以 dp[i][0] = dp[i-1][0];dp[i][0]=dp[i−1][0];
# 最后对二者取最大，即 dp[ i ][ 0 ] = max(dp[i-1][1] + price[i], dp[i-1][0]);dp[i][0]=max(dp[i−1][1]+price[i],dp[i−1][0]);
# dp[i][1]dp[i][1] 表示第 ii 天持有股票
#
# 它可能是第 i-1i−1 天就持有股票，然后第 ii 天没有卖出（也就是在第 ii 天啥也没干），所以 dp[i][1] = dp[i-1][1];dp[i][1]=dp[i−1][1];
# 也可能是第 i-2i−2 天未持有股票，然后第 ii 天买入，所以 dp[i][1] = dp[i-2][0] - price[i];dp[i][1]=dp[i−2][0]−price[i]; （这里有疑问的话，后面会解释）
# 最后对二者取最大，即 dp[i][0] = max(dp[i-1][1], dp[i-2][0] - price[i]);dp[i][0]=max(dp[i−1][1],dp[i−2][0]−price[i]);
# 解释
# 为什么 dp[i][1]dp[i][1] 是由 dp[i-2][0] - price[i]dp[i−2][0]−price[i] 转移过来，而不是由 dp[i-1][0] - price[i]dp[i−1][0]−price[i] 转移过来呢？
#
# 因为 dp[i-1][0]dp[i−1][0] 表示第 i-1i−1 天，也就是第 ii 天的前一天未持有股票。其中包含的一种可能是第 i-1i−1 天卖出了股票，由于题目要求有个冷冻期，所以第 ii 天就不能买入了，也就是说 dp[i][1]dp[i][1] 不能由 dp[i-1][0] - price[i]dp[i−1][0]−price[i] 转移过来，但冷冻期不影响第 i-2i−2 天操作和第 ii 天的操作，所以 dp[i][1]dp[i][1] 可以由 dp[i-2][0] - price[i]dp[i−2][0]−price[i] 转移过来.
#
# 作者：huwt
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/309-zui-jia-mai-mai-gu-piao-shi-ji-han-leng-don-21/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from typing import List
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		length = len(prices)
		if length <= 1:
			return 0
		dp = [[0] * 2 for _ in range(length+1)]
		dp[0][0] = 0
		dp[0][1] = 0
		dp[1][0] = 0
		dp[1][1] = -prices[0]
		for i in range(2, length+1):
			dp[i][0] = max(dp[i-1][1] + prices[i-1], dp[i-1][0])
			dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1])
		return dp[length][0]


if __name__ == "__main__":
	nums = [1, 2, 3, 0, 2]
	print(Solution().maxProfit(nums))
	pass