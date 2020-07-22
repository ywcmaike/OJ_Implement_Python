# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/22 下午11:07

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        i, j = 0, length-1
        while i < j:
            mid = (i+j) // 2
            if nums[mid] < nums[j]:
                j = mid
            elif nums[mid] > nums[j]:
                i = mid+1
            else:
                j -= 1
        return nums[i]