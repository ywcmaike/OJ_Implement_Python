# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/14 下午4:38

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

# idea
# 方法二：双向队列
# 直觉
#
# 如何优化时间复杂度呢？首先想到的是使用堆，因为在最大堆中 heap[0] 永远是最大的元素。在大小为 k 的堆中插入一个元素消耗 \log(k)log(k) 时间，因此算法的时间复杂度为 {O}(N \log(k))O(Nlog(k))。
#
# 能否得到只要 {O}(N)O(N) 的算法？
#
# 我们可以使用双向队列，该数据结构可以从两端以常数时间压入/弹出元素。
#
# 存储双向队列的索引比存储元素更方便，因为两者都能在数组解析中使用。
#
# 算法
#
# 算法非常直截了当：
#
# 处理前 k 个元素，初始化双向队列。
#
# 遍历整个数组。在每一步 :
#
# 清理双向队列 :
#
#   - 只保留当前滑动窗口中有的元素的索引。
#
#   - 移除比当前元素小的所有元素，它们不可能是最大的。
# 将当前元素添加到双向队列中。
# 将 deque[0] 添加到输出中。
# 返回输出数组。
#
# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetcode-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

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
	# nums = [1, 3, -1, -3, 5, 3, 6, 7]
	# k = 3
	# nums = [7, 2, 4]
	# k = 2

	nums = [1, 3, 1, 2, 0, 5]
	k = 3

	print(Solution().maxSlidingWindow(nums, k))
	pass