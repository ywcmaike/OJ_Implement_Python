#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/22 下午7:41

# {0,3}[give|show]{0,3}me{0,3}[the](money|cash){0,5}
# [show)me[the](money|cash)
# {5, 0}(money|cash){0,5}
# ( | money)

# 1
# 0
# 0
# 0
import sys

def isValid(line):
    length = len(line)
    l1 = line.count('{')
    r1 = line.count('}')

    l2 = line.count('[')
    r2 = line.count(']')

    l3 = line.count('(')
    r3 = line.count(')')

    l4 = line.count(',')
    l5 = line.count('|')
    # print(l1, l2, l3, r1, r2, r3)
    if l1 != r1 or l2 != r2 or l3 != r3:
        return 0
    if l1 == l2 == l3 == l4 == l5 == r1 == r2 == r3 == 0:
        return 1
    i = 0
    preline = line
    while i < length-1:
        if preline[i] == '{':
            r1_index = preline[i+1:].index('}')
            if r1_index < 3:
                return 0

            elif ',' in preline[i+1:r1_index+1+i+1]:
                l4_index = line[i+1:r1_index+1+i+1].index(',')
                if l4_index <= 1 or r1_index - l4_index <=1:
                    return 0
                if int(line[i+1:l4_index]) <= int(line[l4_index+1:r1_index]):
                    continue
                else:
                    return 0
            i += r1_index+1
            print(i)
        if line[i] == '[':
            r2_index = line[i+1:].index(']')
            if r2_index - i < 1:
                return 0
            elif '|' in line[i+1:, r2_index]:
                l5_index = line[i+1:r2_index].index('|')
                if l5_index -i <=1 or r2_index - l5_index <= 1:
                    return 0
            i = r2_index + 1
            print(i)
        if line[i] == '(':
            r3_index = line[i + 1:].index(')')
            if r3_index - i < 1:
                return 0
            elif '|' in line[i + 1:, r3_index]:
                l5_index = line[i + 1:r3_index].index('|')
                if l5_index - i <= 1 or r3_index - l5_index <= 1:
                    return 0
            i = r2_index + 1
            print(i)
    return 1





if __name__ == '__main__':
    # 读取第一行的n
    while True:
        # 读取每一行
        line = sys.stdin.readline().strip()
        print(isValid(line))
