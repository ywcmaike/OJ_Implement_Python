# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/13 下午2:46

# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
#
#  
#
# 示例 1：
#
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
# 示例 2：
#
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        if length < 4:
            return []
        nums_dict = {}
        for i in range(length):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1
        for k, v in nums_dict.items():
            if v == 1:
                result.append(k)
        return result

# fast
# 相同的数异或为0，不同的异或为1。0和任何数异或等于这个数本身。
#
# 所以，数组里面所有数异或 = 目标两个数异或 。 由于这两个数不同，所以异或结果必然不为0。
#
# 假设数组异或的二进制结果为10010，那么说明这两个数从右向左数第2位是不同的
#
# 那么可以根据数组里面所有数的第二位为0或者1将数组划分为2个。
#
# 这样做可以将目标数必然分散在不同的数组中，而且相同的数必然落在同一个数组中。
#
# 这两个数组里面的数各自进行异或，得到的结果就是答案
class SolutionFast:
	def singleNumbers(self, nums: List[int]) -> List[int]:
		ret, index = 0, 0
		for n in nums:
			ret ^= n
			# print(ret)
		# 找从右向左数第几位不同，也就是第index位
		# 这一步其实可以根据n & (-n)的快捷方式获得，不过对位运算掌握不是那么熟练的话，记结论容易忘，不如理解实质
		while ret & 1 == 0:
			index += 1
			ret >>= 1
			# print(ret)
		r1, r2 = 0, 0
		for n in nums:
			if (n >> index) & 1 == 0:
				r1 ^= n
				# print(r1)
			else:
				r2 ^= n
				# print(r2)
		return [r1, r2]


if __name__ == "__main__":
	nums = [4, 1, 4, 6]
	print(SolutionFast().singleNumbers(nums))
	pass