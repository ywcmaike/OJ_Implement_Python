#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:maike
# datetime:2020/6/24 下午11:36

# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-strstr
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
# idea KMP
# 先在开头约定，本文用 pat 表示模式串，长度为 M，txt 表示文本串，长度为 N。KMP 算法是在 txt 中查找子串 pat，如果存在，返回这个子串的起始索引，否则返回 -1
# 为什么说 KMP 算法和状态机有关呢？是这样的，我们可以认为 pat 的匹配就是状态的转移
# KMP 算法最关键的步骤就是构造这个状态转移图。要确定状态转移的行为，得明确两个变量，一个是当前的匹配状态，另一个是遇到的字符；确定了这两个变量后，就可以知道这个情况下应该转移到哪个状态。
# 为了描述状态转移图，我们定义一个二维 dp 数组，它的含义如下：
#
# dp[状态][字符] = 下个状态
# dp[j][c] = next
# 0 <= j < M，代表当前的状态
# 0 <= c < 256，代表遇到的字符（ASCII 码）
# 0 <= next <= M，代表下一个状态
#
# dp[4]['A'] = 3 表示：
# 当前是状态 4，如果遇到字符 A，
# pat 应该转移到状态 3
#
# dp[1]['B'] = 2 表示：
# 当前是状态 1，如果遇到字符 B，
# pat 应该转移到状态 2
# 根据我们这个 dp 数组的定义和刚才状态转移的过程，我们可以先写出 KMP 算法的 search 函数代码：
#

# 传统的 KMP 算法是使用一个一维数组 next 记录前缀信息，而本文是使用一个二维数组 dp 以状态转移的角度解决字符匹配问题，但是空间复杂度仍然是 O(256M) = O(M)。
#
# 在 pat 匹配 txt 的过程中，只要明确了「当前处在哪个状态」和「遇到的字符是什么」这两个问题，就可以确定应该转移到哪个状态（推进或回退）。
#
# 对于一个模式串 pat，其总共就有 M 个状态，对于 ASCII 字符，总共不会超过 256 种。所以我们就构造一个数组 dp[M][256] 来包含所有情况，并且明确 dp 数组的含义：
#
# dp[j][c] = next 表示，当前是状态 j，遇到了字符 c，应该转移到状态 next。
#
# 明确了其含义，就可以很容易写出 search 函数的代码。
#
# 对于如何构建这个 dp 数组，需要一个辅助状态 X，它永远比当前状态 j 落后一个状态，拥有和 j 最长的相同前缀，我们给它起了个名字叫「影子状态」。
#
# 在构建当前状态 j 的转移方向时，只有字符 pat[j] 才能使状态推进（dp[j][pat[j]] = j+1）；而对于其他字符只能进行状态回退，应该去请教影子状态 X 应该回退到哪里（dp[j][other] = dp[X][other]，其中 other 是除了 pat[j] 之外所有字符）。
#
# 对于影子状态 X，我们把它初始化为 0，并且随着 j 的前进进行更新，更新的方式和 search 过程更新 j 的过程非常相似（X = dp[X][pat[j]]）。
#
# 作者：labuladong
# 链接：https://leetcode-cn.com/problems/implement-strstr/solution/kmp-suan-fa-xiang-jie-by-labuladong/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class SolutionKMP:

    def strStr(self, txt: str, pat: str) -> int: # search


        def gen_pnext(pat: str):
            k = -1
            pnext = [-1] * len(pat)
            i = 0
            while i < len(pat) -1:
                if k == -1 or pat[i] == pat[k]:
                    k += 1
                    i += 1
                    if pat[i] == pat[k]:
                        pnext[i] = pnext[k]
                    else:
                        pnext[i] = k
                else:
                    k = pnext[k]
            return pnext

        pnext = gen_pnext(pat)
        m, n = len(pat), len(txt)
        i, j = 0, 0
        while i < n and j < m:
            if txt[i] == pat[j] or j == -1:
                i += 1
                j += 1
            else:
                j = pnext[j]
        if j == m:
            return i - m
        else:
            return -1





if __name__ == '__main__':
    # haystack = "hello"
    # needle = "ll"
    haystack = "aabbaaa"
    needle = "bba"

    haystack = "aa"
    needle = "aa"

    solution = SolutionKMP()
    print(solution.strStr(haystack, needle))