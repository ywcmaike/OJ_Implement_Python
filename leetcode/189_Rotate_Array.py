#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/8 上午12:27

# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Follow up:
#
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# idea
# 取余,求得rotation,
# 观察变化

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