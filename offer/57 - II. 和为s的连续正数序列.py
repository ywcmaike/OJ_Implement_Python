# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/15 下午2:21

# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#
#  
#
# 示例 1：
#
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 示例 2：
#
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
class Solution:
	def findContinuousSequence(self, target: int) -> List[List[int]]:
		if target < 3:
			return []
		res = []
		for n in range(2, target+1):
			temp = target - n*(n-1)//2
			if temp <= 0:
				break
			if not temp % n:
				start = temp // n
				res.append([start+i for i in range(n)])
		# print(res)
		return res[::-1]

class SolutionDP:
	def findContinuousSequence(self, target: int) -> List[List[int]]:
		if target < 3:
			return []
		res = []
		l, r = 1, 2
		while l < r:
			cursum = (l+r)*(r-l+1)/2
			if cursum == target:
				res.append([i for i in range(l, r+1)])
				l += 1
			elif cursum < target:
				r += 1
			else:
				l += 1
		return res



if __name__ == "__main__":
	print(SolutionDP().findContinuousSequence(15))
	pass