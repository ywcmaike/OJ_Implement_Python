# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/13 下午3:28

# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
#
# 示例 1：
#
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1
# 示例 2:
#
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea
# 数论
#
# 任何大于1的数都可由2和3相加组成（根据奇偶证明）
# 因为2*2=1*4，2*3>1*5, 所以将数字拆成2和3，能得到的积最大
# 因为2*2*2<3*3, 所以3越多积越大 时间复杂度O(n/3)，用幂函数可以达到O(log(n/3)), 因为n不大，所以提升意义不大，我就没用。 空间复杂度常数复杂度O(1)
# 双百解法，简单的数论题，DP并不是最优解，套用DP谁都会，而数论会让面试官眼前一亮(尤其如果面试官水平一般的话，只认为DP才能解，数论时间复杂度空间复杂度都远胜DP，
# 他就会怀疑正确性，你即使告诉他怎么证明的，他也会拉着你的代码逐行带入计算，最后被震惊的话，恭喜你幸运的拿到一个SH)。

from typing import List
class Solution:
	def cuttingRope(self, n: int) -> int:
		if n <= 3:
			return n - 1
		div = n // 3
		rem = n % 3
		if rem == 2:
			return pow(3, div) * pow(2, rem//2)
		elif rem == 1:
			return pow(3, div-1) * pow(2, (rem + 3)//2)
		else:
			return pow(3, div)





if __name__ == "__main__":
	print(Solution().cuttingRope(10))
	pass