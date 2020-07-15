# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/16 上午12:38


#  在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
#
#  
#
# 示例 1：
#
# 输入：nums = [3,4,3,3]
# 输出：4
# 示例 2：
#
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea
# 原理：[A,A,A,B,B,B,C,C,C] 和 [A,A,A,B,B,B,C]，差了两个C。即：
#
# 3×(a b c)−(a a a b b b c)=2c
#
# 也就是说，如果把原数组去重、再乘以3得到的值，刚好就是要找的元素的2倍。
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int((sum(set(nums))*3 - sum(nums))//2)

if __name__ == "__main__":
	pass