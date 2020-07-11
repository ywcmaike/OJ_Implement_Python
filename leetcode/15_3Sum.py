# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/11 下午5:42

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# idea
# 首先将数组排序，然后从左到右遍历这个数组。在当前遍历的值右边找到两个数加和等于当前值的相反数。
# 由于是要三个数加和等于0，那么一定有一个数小于0，所以只需要遍历到小于等于0的区域

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            find_num = -nums[i]
            while L < R:
                if L > i+1 and nums[L] == nums[L-1]:
                    L += 1
                    continue
                if R < len(nums) - 1 and nums[R] == nums[R+1]:
                    R -= 1
                    continue
                if nums[L] + nums[R] > find_num:
                    R -= 1
                elif nums[L] + nums[R] < find_num:
                    L += 1
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
        return result

if __name__ == "__main__":
	nums = [-1, 0, 1, 2, -1, -4]
	print(Solution().threeSum(nums))
	pass