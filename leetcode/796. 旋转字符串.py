# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/15 下午4:03

# 给定两个字符串, A 和 B。
#
# A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。
#
# 示例 1:
# 输入: A = 'abcde', B = 'cdeab'
# 输出: true
#
# 示例 2:
# 输入: A = 'abcde', B = 'abced'
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea
# 只需要判断 B 是否为 A + A 的子串就可以了：

from typing import List
class Solution:
	def rotateString(self, A: str, B: str) -> bool:
		return len(A) == len(B) and (B in A*2)

# idea KMP
# 先在开头约定，本文用 pat 表示模式串，长度为 M，txt 表示文本串，长度为 N。KMP 算法是在 txt 中查找子串 pat，如果存在，返回这个子串的起始索引，否则返回 -1
# 为什么说 KMP 算法和状态机有关呢？是这样的，我们可以认为 pat 的匹配就是状态的转移
# KMP 算法最关键的步骤就是构造这个状态转移图。要确定状态转移的行为，得明确两个变量，一个是当前的匹配状态，另一个是遇到的字符；确定了这两个变量后，就可以知道这个情况下应该转移到哪个状态。
# 为了描述状态转移图，我们定义一个二维 dp 数组，它的含义如下：
#
#
# dp[j][c] = next
# 0 <= j < M，代表当前的状态
# 0 <= c < 256，代表遇到的字符（ASCII 码）
# 0 <= next <= M，代表下一个状态
#
# dp[4]['A'] = 3 表示：
# 当前是状态 4，如果遇到字符 A，
# pat 应该转移到状态 3
#
# dp[1]['B'] = 2 表示：
# 当前是状态 1，如果遇到字符 B，
# pat 应该转移到状态 2
# 根据我们这个 dp 数组的定义和刚才状态转移的过程，我们可以先写出 KMP 算法的 search 函数代码：
#



if __name__ == "__main__":
	A = 'abcde'
	B = 'cdeab'
	print(Solution().rotateString(A, B))
	pass