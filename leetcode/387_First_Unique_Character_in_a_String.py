# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午10:52

# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
# Note: You may assume the string contains only lowercase English letters.

from typing import  List

class Solution:
	def firstUniqChar(self, s: str) -> int:
		s_index = {}
		for i in range(len(s)):
			s_index[s[i]] = i
		print(s_index)
		for i in range(len(s)):
			if i == s_index[s[i]]:
				return i
			else:
				s_index[s[i]] = -1
		return -1



if __name__ == "__main__":
	# s = "leetcode"
	s = "loveleetcode"
	print(Solution().firstUniqChar(s))



