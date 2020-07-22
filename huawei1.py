#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/22 下午6:32

# 5
# 2 10 10
# 4 10 15 20 30
# 5 10 10 10 10 10
# 6 10 20 20 70 10 10
# 8 10 120 10 10 10 10 10 10

import sys

def isValid(lst):
    n = lst[0]
    if n < 1:
        return 1
    count_dict = {}
    sum_num = 0
    for i in range(1, n+1):
        sum_num += lst[i]
        j = sum_num // 60
        if j not in count_dict:
            count_dict[j] = 1
        else:
            count_dict[j] += 1
        if count_dict[j] > 4:
            return 0
    return 1



if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        print(isValid(values))
