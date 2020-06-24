#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/6/24 下午11:36

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        for i in range(0, len(haystack)-len(needle) + 1):
            if str(haystack[i:i+len(needle)]) == str(needle):
                return i
            else:
                pass
        return -1


if __name__ == '__main__':
    # haystack = "hello"
    # needle = "ll"
    haystack = "aabbaaa"
    needle = "bba"

    # haystack = "aa"
    # needle = "aa"

    solution = Solution()
    print(solution.strStr(haystack, needle))