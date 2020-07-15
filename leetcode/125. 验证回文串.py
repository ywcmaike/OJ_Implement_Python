# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/15 下午3:51

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-palindrome
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea

from typing import List
class Solution:
	def isPalindrome(self, s: str) -> bool:
		s = list(filter(str.isalnum, s.lower()))
		# print(s)
		return s == s[::-1]

class SolutionDP:
	def isPalindrome(self, s: str) -> bool:
		s = s.lower()
		length = len(s)
		i, j = 0, length-1
		while i < j:
			if not((s[i] >= '0' and s[i] <= '9') or (s[i] >= 'a' and s[i] <= 'z')):
				i += 1
				continue
			if not((s[j] >= '0' and s[j] <= '9') or (s[j] >= 'a' and s[j] <= 'z')):
				j -= 1
				continue
			if s[i] != s[j]:
				return False
			i += 1
			j -= 1
		return True

if __name__ == "__main__":
	s = "A man, a plan, a canal: Panama"
	print(SolutionDP().isPalindrome(s))
	pass