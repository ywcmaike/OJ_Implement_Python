#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/8 上午1:24

# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# idea
# 从有向左逐字符加一,判断进位条件

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        addone = 0
        for i in range(len(digits)):
            if i == 0:
                addone = 1
            if addone:
                if digits[-i-1] + 1 != 10:
                    digits[-i-1] += 1
                    return digits
                    addone = 0
                else:
                    digits[-i-1] = 0
                    if i + 2 > len(digits):
                        return [1] + digits
                    addone = 1
            else:
                break



if __name__ == '__main__':
    digits = [9, 9, 9, 9]
    print(Solution().plusOne(digits))