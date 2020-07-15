# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/15 下午7:32
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 示例 1:
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  示例 2:
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		result = []
		len_s = len(s)
		len_p = len(p)
		if len_s < 1 or len_p < 1 or len_s < len_p:
			return []
		count_s = [0] * 26
		count_p = [0] * 26
		for a in p:
			count_p[ord(a) - 97] += 1
		left = 0
		for right in range(len_s):
			if right < len_p - 1:
				count_s[ord(s[right])-97] += 1
				continue
			count_s[ord(s[right])-97] += 1
			if count_s == count_p:
				result.append(left)
			count_s[ord(s[left])-97] -= 1
			left += 1
		return result







if __name__ == "__main__":
	s = "cbaebabacd"
	p = "abc"
	print(Solution().findAnagrams(s, p))
	pass