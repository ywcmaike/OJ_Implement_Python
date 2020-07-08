#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/8 上午12:27

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[(len(nums) - k % (len(nums))):] + nums[: (len(nums) - k % (len(nums)))]
        print(nums)
        # return nums

        # len_nums = len(nums)
        # for i in range(k % len_nums):
        #     nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    # nums = [-1, -100, 3, 99]
    # k = 2
    solution = Solution()
    solution.rotate(nums, k)