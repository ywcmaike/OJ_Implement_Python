# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/14 下午9:58

# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#  
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？
#
#  
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

from collections import deque

class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		length = len(nums)
		if length * k == 0:
			return []
		if k == 1:
			return nums
		deq = deque()
		result = []
		for i in range(length):
			while len(deq) > 0 and nums[deq[-1]] <= nums[i]:
				deq.pop()
			deq.append(i)
			if deq[0] <= i-k:
				deq.popleft()
			if i+1 >= k:
				result.append(nums[deq[0]])
		return result




if __name__ == "__main__":
	nums = [1,3,-1,-3,5,3,6,7]
	k = 3
	print(Solution().maxSlidingWindow(nums, k))
	pass