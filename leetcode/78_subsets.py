#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/6/24 下午11:56

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for i in nums:
            for j in range(len(results)):
                c = results[j].copy()
                c.append(i)
                results.append(c)
        return results

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.subsets(nums))
    pass

