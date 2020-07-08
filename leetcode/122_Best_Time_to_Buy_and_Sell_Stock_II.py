#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/7 下午11:25

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                result += prices[i + 1] - prices[i]
        return result



if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    prices = [1,2,3,4,5]
    # prices = [7,6,4,3,1]
    solution = Solution()
    print(solution.maxProfit(prices))
    pass