# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/13 下午4:30

# 给定两个数组，编写一个函数来计算它们的交集。
#
#  
#
# 示例 1：
#
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 示例 2:
#
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
#  
#
# 说明：
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。
# 进阶：
#
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 < 1 or length2 < 1:
            return []
        num1_dict = {}
        num2_dict = {}
        for i in nums1:
            if i not in num1_dict:
                num1_dict[i] = 1
            else:
                num1_dict[i] += 1
        for j in nums2:
            if j not in num2_dict:
                num2_dict[j] = 1
            else:
                num2_dict[j] += 1
        result = []
        for k, v in num1_dict.items():
            if k in num2_dict:
                for i in range(min(num2_dict[k], v)):
                    result.append(k)
        return result
class SolutionSet:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 < 1 or length2 < 1:
            return []
        inter = set(nums1) & set(nums2)
        result = []
        for i in inter:
            result += [i] * min(nums1.count(i), nums2.count(i))
        return result

if __name__ == "__main__":
	pass