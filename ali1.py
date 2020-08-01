#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/24 下午7:14

import sys

def maxEat(n, nums):
    if n <= 0:
        return 0
    if n == 1:
        return nums[0]
    ans = 0
    while (len(nums) > 0):
        min_num = min(nums)
        ans += min_num * len(nums)
        nums = [i - min_num for i in nums]
        zero_index = nums.index(0)
        nums[:] = nums[:zero_index]
        # print(nums)
    return ans



if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    # print(n, values)
    print(maxEat(n, values))
