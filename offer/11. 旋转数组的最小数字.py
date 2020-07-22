# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/22 下午11:03

# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
#
# 示例 1：
#
# 输入：[3,4,5,1,2]
# 输出：1
# 示例 2：
#
# 输入：[2,2,2,0,1]
# 输出：0
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List

class Solution:
	def minArray(self, numbers: List[int]) -> int:
		length = len(numbers)
		if length == 1:
			return numbers[0]
		i, j = 0, length - 1
		while i < j:
			mid = (i + j) // 2
			if numbers[mid] < numbers[j]:
				j = mid
			elif numbers[mid] > numbers[j]:
				i = mid+1
			else:
				j -= 1
		return numbers[i]

if __name__ == "__main__":
	# numbers = [3,4,5,1,2]
	numbers = [2,2,2,0,1]
	print(Solution().minArray(numbers))
	pass