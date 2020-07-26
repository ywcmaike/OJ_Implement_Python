# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/23 下午11:14

# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#  
#
# 示例2:
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutation-in-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
import collections
class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		l1, l2 = len(s1), len(s2)
		c1 =
if __name__ == "__main__":
	s1 = "ab"
	s2 = "eidboaoo"
	print(Solution().checkInclusion(s1, s2))
	pass