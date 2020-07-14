# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/13 下午2:42

# 找出数组中重复的数字。
#
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#
# 示例 1：
#
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        length = len(nums)
        if length <2:
            return -1
        num_dict = {}
        for i in range(length):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = 1
            else:
                return nums[i]

if __name__ == "__main__":
	pass