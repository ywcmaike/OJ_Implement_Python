#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/7/7 下午10:32

from typing import List
import sys


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) < 1:
            return result
        min_str = strs[0]
        flag = True
        while len(min_str) > 0:
            for i in range(1, len(strs)):
                if strs[i][:len(min_str)] != min_str:
                    min_str = min_str[:-1]
                    flag = False
                    break
            if flag == True:
                result = min_str
                break
            else:
                flag = True
        return result


if __name__ == '__main__':
    # strs = ["flower","flow","flight"]
    # strs = ['ada', 'ad']
    # strs = ["dog","racecar","car"]
    # strs = ['ca', 'a']
    strs = ["c", "acc", "ccc"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))