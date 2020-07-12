# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/12 下午11:48

# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 示例 2:
#
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea
# 对于任意一天考虑四个变量:
# fstBuy: 在该天第一次买入股票可获得的最大收益
# fstSell: 在该天第一次卖出股票可获得的最大收益
# secBuy: 在该天第二次买入股票可获得的最大收益
# secSell: 在该天第二次卖出股票可获得的最大收益
# 分别对四个变量进行相应的更新, 最后secSell就是最大
# 收益值(secSell >= fstSell)


from typing import List
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		length = len(prices)
		if length < 2:
			return 0
		fstBuy, fstSell = float("-inf"), 0
		secBuy, secSell = float("-inf"), 0
		for p in prices:
			fstBuy = max(fstBuy, -p)
			fstSell = max(fstSell, fstBuy+p)
			secBuy = max(secBuy, fstSell-p)
			secSell = max(secSell, secBuy+p)
		return secSell

class SolutionDP:
	def maxProfit(self, prices: List[int]) -> int:
		length = len(prices)
		if length < 2:
			return 0




if __name__ == "__main__":
	# nums = [3, 3, 5, 0, 0, 3, 1, 4]
	# nums = [1,2,3,4,5]
	nums = [7,6,4,3,1]
	# nums = [6,1,3,2,4,7]
	print(Solution().maxProfit(nums))
	pass