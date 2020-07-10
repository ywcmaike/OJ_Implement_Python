# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午10:43

# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
#
#
# Example 1:
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
#
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
from typing import List

class Solution:
	def reverseString(self, s: List[str]) -> None:
		"""
        Do not return anything, modify s in-place instead.
        """
		if len(s) > 1:
			for i in range(len(s) // 2):
				s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
		# print(s)

if __name__ == "__main__":

	# s =["h","e","l","l","o"]
	s = ["H","a","n","n","a","h"]
	s = []
	s = ['1']
	print(s)
	print(Solution().reverseString(s))