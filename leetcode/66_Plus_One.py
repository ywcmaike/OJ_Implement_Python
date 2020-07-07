#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/8 上午1:24


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