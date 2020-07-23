#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/22 下午7:44

# 将数组分成两组，使两组的和的差的绝对值最小
# 3
# 17 8 11

# 19
import sys

class Solution:
    def findSize(self, n, nums):
        if n < 1:
            return 0
        if n == 1:
            return nums[0]
        cursum = sum(nums)
        harfsum = cursum // 2
        dp = [[0] * (harfsum+1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, harfsum+1):
                if j >= nums[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]] + nums[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        return max(cursum - dp[n][harfsum], dp[n][harfsum])


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(n, values)
    print(Solution().findSize(n, values))
    