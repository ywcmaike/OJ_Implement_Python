#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/8 上午1:55


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i in range(len(nums)):
            hash_dict[nums[i]] = i
        for i in range(len(nums)):
            if (target-nums[i]) in hash_dict and hash_dict[target-nums[i]] != i:
                return [i, hash_dict[target-nums[i]]]
        return []

if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    # target = 22
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))