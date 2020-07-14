# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/14 下午4:16

# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 注意：
#
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-consecutive-ones
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 1:
            return 0
        count = 0
        maxcount = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > maxcount:
                    maxcount = count
            else:
                count = 0
        return maxcount
if __name__ == "__main__":
	pass