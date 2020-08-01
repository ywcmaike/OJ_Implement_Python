#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/24 下午7:36

# 3
# 3 2
# 01 11 10
# 11 00 10
# 2 3
# 101 111
# 010 001
# 2 2
# 01 10
# 10 01

import sys

def transform(matNL, final_matNL):
    n, L = len(matNL), len(matNL[0])





if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = ''
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        NL = list(map(int, line.split()))
        N, L = NL[0], NL[1]
        matNL = [[0]*L for _ in range(N)]
        line = sys.stdin.readline().strip()
        values = list(map(str, line.split()))
        for i in range(N):
            matNL[i] = list(map(int, values[i]))
        # print(matNL)
        final_matNL = [[0] * L for _ in range(N)]
        line = sys.stdin.readline().strip()
        values = list(map(str, line.split()))
        for i in range(N):
            final_matNL[i] = list(map(int, values[i]))
        # print(final_matNL)

        # if i < n-1:
        #     ans += (str(transform(matNL, final_matNL))+str('\n'))
        # else:
        print(str(transform(matNL, final_matNL)))


        # for v in values:
        #     ans += v
    # print(ans)
    