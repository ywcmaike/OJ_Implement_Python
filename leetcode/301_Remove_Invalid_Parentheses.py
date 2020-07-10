# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午10:40

# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Example 1:
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:
#
# Input: ")("
# Output: [""]

from typing import List

class Solution:
	def removeInvalidParentheses(self, s: str) -> List[str]:
		pass


if __name__ == "__main__":
	s = "()())()"
	s = "(a)())()"
	s = ")("
	print(Solution().removeInvalidParentheses(s))
