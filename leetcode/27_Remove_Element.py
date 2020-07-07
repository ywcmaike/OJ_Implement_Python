#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/8 上午1:01

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while (i < len(nums)):
            if val == nums[i]:
                nums[:] = nums[:i] + nums[i+1:]
            else:
                i += 1
        return len(nums)

if __name__ == '__main__':
    # nums = [3,2,2,3]
    # val = 3
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(Solution().removeElement(nums, val))

