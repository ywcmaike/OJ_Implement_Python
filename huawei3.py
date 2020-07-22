#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/22 下午7:44

# 3
# 17 8 11

# 19
import sys

def findSize(n, nums):
    if n < 1:
        return 0
    nums.sort()
    print(nums)
    for i in range(n):
        j, k = i, n-1
        if sums



    return 0


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(findSize(n, values))
    