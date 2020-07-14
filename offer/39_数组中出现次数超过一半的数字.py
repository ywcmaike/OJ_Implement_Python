# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/12 下午11:01

# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
#  
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#  
#
# 示例 1:
#
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		nums.sort()
		return nums[len(nums) // 2]

if __name__ == "__main__":
	nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
	print(Solution().majorityElement(nums))
	pass